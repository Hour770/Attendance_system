import atexit
import csv
import os
from datetime import datetime, timedelta

import cv2
import numpy as np
from face_encoding import load_encodings
from flask import Flask, Response, redirect, render_template, request, url_for

import face_recognition

app = Flask(__name__)

# Load known face encodings and names
known_face_encodings, known_face_names, known_face_genders = load_encodings()  # Call the function with gender data

already_marked = set()  # To keep track of already marked attendees

# Variables
video_capture = None
current_date = datetime.now().strftime("%Y-%m-%d")
attendance_file_path = f"data/{current_date}.csv"
csv_writer = None
attendance_file = None

# Set the class start time (configurable)
class_start_time_str = "13:20" #set the start time class as HH:MM
class_start_time = datetime.strptime(class_start_time_str, "%H:%M").time()

def initialize_csv():
    """
    Initialize or load the attendance CSV file for the current day.
    """
    global attendance_file, csv_writer, already_marked

    os.makedirs('data', exist_ok=True)  # Ensure the data folder exists

    if not os.path.exists(attendance_file_path):
        attendance_file = open(attendance_file_path, "w+", newline="")
        csv_writer = csv.writer(attendance_file)
        csv_writer.writerow(["Name", "Gender", "Time", "Status"])
    else:
        attendance_file = open(attendance_file_path, "a", newline="")
        csv_writer = csv.writer(attendance_file)
        # Load already marked attendees from the file
        with open(attendance_file_path, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) >= 4 and row[0] != "Name":  # Skip header and incomplete rows
                    already_marked.add(row[0])


def auto_save_and_close():
    """
    Automatically save and close the attendance file when the app stops.
    """
    global attendance_file
    if attendance_file:
        attendance_file.close()

# Ensure the attendance file is saved when the application exits
atexit.register(auto_save_and_close)


def generate_frames():
    """
    Capture video frames, detect faces, and mark attendance.
    """
    global already_marked, csv_writer

    event_start_time = datetime.now()

    while True:
        ret, frame = video_capture.read()
        if not ret:
            break

        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            name = "Unknown"

            if face_distances[best_match_index] < 0.4:
                name = known_face_names[best_match_index]
            elif face_distances[best_match_index] < 0.6:  # Ambiguous match
                name = "Unknown"
            else:
                name = "Unknown"

            face_names.append(name)
            if name in known_face_names and name not in already_marked:
                already_marked.add(name)
                current_time = datetime.now()
                time_difference = current_time - event_start_time
                status = "On-time"
                
                class_start_datetime = datetime.combine(current_time.date(), class_start_time)
                time_difference = current_time - class_start_datetime

                # Determine the attendance status
                if time_difference <= timedelta(minutes=15):
                    status = "On-time"
                elif time_difference <= timedelta(minutes=60):
                    status = "Late"
                else:
                    status = "Absent"
                # Get gender based on name
                gender = known_face_genders.get(name, "Unknown")

                # Write the status to the CSV, including gender
                csv_writer.writerow([name, gender, current_time.strftime("%H:%M:%S"), status ])

        for (top, right, bottom, left), name in zip(face_locations, face_names):
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            if name == "Unknown":
                frame_color = (0, 0, 255)  # Red for unknown
                text_color = (0, 0, 0)    # Black text for readability
            else:
                frame_color = (0, 255, 0)  # Green for recognized
                text_color = (0, 0, 0) # Black text for readability

            cv2.rectangle(frame, (left, top), (right, bottom), frame_color, 2)
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), frame_color, cv2.FILLED)
            cv2.putText(frame, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_SIMPLEX, 0.5, text_color, 1)

        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/start_attendance')
def start_attendance():
    global video_capture
    if video_capture is None or not video_capture.isOpened():
        video_capture = cv2.VideoCapture(0)
        initialize_csv()
    return render_template('attendance.html')


@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/stop_attendance')
def stop_attendance():
    global video_capture
    if video_capture and video_capture.isOpened():
        video_capture.release()
    auto_save_and_close()
    return redirect(url_for('index'))


@app.route('/view_log')
def view_log():
    attendance_data = []
    if os.path.exists(attendance_file_path):
        with open(attendance_file_path, "r") as file:
            reader = csv.reader(file)
            next(reader, None)  # Skip header
            for row in reader:
                if len(row) >= 4:  # Ensure the row has at least 4 elements
                    attendance_data.append({"name": row[0], "gender": row[1], "status": row[2], "time": row[3]})
    return render_template('log.html', attendance=attendance_data)


@app.route('/view_log_by_date', methods=['POST'])
def view_log_by_date():
    selected_date = request.form['date']
    selected_file_path = f"data/{selected_date}.csv"

    attendance_data = []
    if os.path.exists(selected_file_path):
        with open(selected_file_path, "r") as file:
            reader = csv.reader(file)
            next(reader, None)  # Skip header
            for row in reader:
                if len(row) >= 4:  # Ensure the row has at least 4 elements
                    attendance_data.append({"name": row[0], "gender": row[1], "status": row[2], "time": row[3]})

    # Pass the selected date and attendance data to the template
    return render_template('log.html', attendance=attendance_data, selected_date=selected_date)


if __name__ == "__main__":
    app.run(debug=True)
