Overview

This project implements an automatic attendance marking system using face recognition. The system uses a webcam to capture live video, detects faces, and marks attendance based on recognized faces. The system tracks attendance based on the class start time, marking students as "On-time", "Late", or "Absent". It saves attendance data in a CSV file and provides a web interface to view the log.

Features

- Face Recognition: Detects faces from live webcam feed and matches them with a pre-loaded database.
- Attendance Status: Marks students as "On-time", "Late", or "Absent" based on the class start time and their arrival time.
- CSV Logging: Attendance data is saved in a CSV file, with columns for "Name", "Gender", "Time", and "Status".
- Web Interface: Provides an interface to start/stop attendance, view the log, and filter attendance by date.
- Configurable Class Start Time: Allows you to configure the class start time for marking lateness and absence.
- Auto-Save: The attendance file is automatically saved with each new entry, and is properly closed when the app stops.

Requirements
- Python 3.6 or higher
- Flask
- OpenCV
- Face Recognition library
- Numpy

face-recognition/
- app.py
- face_encoding.py
- data/
  - (attendance CSV files will be saved here)
- static/
  - logo.png
  - styles.css
- templates/
  - index.html
  - attendance.html
  - log.html
- README.md


To start the application, run the following command:

python app.py

Navigate to http://127.0.0.1:5000/ in your browser to access the web interface.


Endpoints

- /: Home page.
- /start_attendance: Starts the attendance tracking (activates the webcam and starts marking attendance).
- /stop_attendance: Stops the attendance tracking and saves the attendance to the CSV file.
- /video_feed: Provides a live video feed with face recognition and attendance marking.
- /view_log: Displays the current day's attendance log.
- /view_log_by_date: Allows viewing the attendance log for a specific date (selected through a form).


Web Interface

The web interface consists of the following pages:

- Home Page (/): A simple homepage with buttons to start and stop the attendance system. It displays the logo from static/logo.png and uses custom styling from static/styles.css.
- Attendance Page (/start_attendance): Displays the webcam feed and starts the face recognition attendance system.
- Log Page (/view_log): Displays the attendance log for the current day, showing "Name", "Gender", "Time", and "Status".
- Log by Date Page (/view_log_by_date): Allows users to view the attendance log for a specific date.


Attendance CSV Structure

Attendance is saved in CSV format with the following columns:

- Name: The name of the student.
- Gender: The gender of the student (if available).
- Time: The time at which the student was recognized.
- Status: The student's attendance status, either "On-time", "Late", or "Absent", depending on their arrival time.
