import face_recognition


def load_encodings():
    """
    Load known face encodings and names.
    Returns:
        known_face_encodings (list): A list of face encodings.
        known_face_names (list): A list of names corresponding to each encoding.
        known_face_genders (dict): A dictionary mapping names to gender.
    """
    #replace with user image from your device. up to 10-20 images give more accuracy.
    hour_images = [
        "C:/Users/U-ser/OneDrive - American University of Phnom Penh/Desktop/image/hour.png",
        "C:/Users/U-ser/OneDrive - American University of Phnom Penh/Desktop/image/hour1.png",
        "C:/Users/U-ser/OneDrive - American University of Phnom Penh/Desktop/image/hour2.jpg",
        "C:/Users/U-ser/OneDrive - American University of Phnom Penh/Desktop/image/hour3.png",
        "C:/Users/U-ser/OneDrive - American University of Phnom Penh/Desktop/image/hour4.png",
        "C:/Users/U-ser/OneDrive - American University of Phnom Penh/Desktop/image/hour5.png",
        "C:/Users/U-ser/OneDrive - American University of Phnom Penh/Desktop/image/hour6.png",
        "C:/Users/U-ser/OneDrive - American University of Phnom Penh/Desktop/image/hour7.png",
        "C:/Users/U-ser/OneDrive - American University of Phnom Penh/Desktop/image/hour8.png",
        "C:/Users/U-ser/OneDrive - American University of Phnom Penh/Desktop/image/hour9.png",
        "C:/Users/U-ser/OneDrive - American University of Phnom Penh/Desktop/image/hour10.png",
        "C:/Users/U-ser/OneDrive - American University of Phnom Penh/Desktop/image/hour11.png",
        "C:/Users/U-ser/OneDrive - American University of Phnom Penh/Desktop/image/hour12.png",
        "C:/Users/U-ser/OneDrive - American University of Phnom Penh/Desktop/image/hour13.png",
        "C:/Users/U-ser/OneDrive - American University of Phnom Penh/Desktop/image/hour14.png",
        "C:/Users/U-ser/OneDrive - American University of Phnom Penh/Desktop/image/hour15.png",
        "C:/Users/U-ser/OneDrive - American University of Phnom Penh/Desktop/image/hour16.png",
        "C:/Users/U-ser/OneDrive - American University of Phnom Penh/Desktop/image/hour17.png",
        "C:/Users/U-ser/OneDrive - American University of Phnom Penh/Desktop/image/hour18.png",
        "C:/Users/U-ser/OneDrive - American University of Phnom Penh/Desktop/image/hour19.png",
    ]
    hour_encodings = []
    for image_path in hour_images:
        image = face_recognition.load_image_file(image_path)
        encodings = face_recognition.face_encodings(image)
        if encodings:
            hour_encodings.append(encodings[0])

    messi_images = [
        "C:/Users/U-ser/OneDrive - American University of Phnom Penh/Desktop/image/messi1.jpg",
        "C:/Users/U-ser/OneDrive - American University of Phnom Penh/Desktop/image/messi2.webp",
        "C:/Users/U-ser/OneDrive - American University of Phnom Penh/Desktop/image/messi3.jpg",
        "C:/Users/U-ser/OneDrive - American University of Phnom Penh/Desktop/image/messi4.jpg",
        "C:/Users/U-ser/OneDrive - American University of Phnom Penh/Desktop/image/messi5.jpg",
        "C:/Users/U-ser/OneDrive - American University of Phnom Penh/Desktop/image/messi6.jpg",
        "C:/Users/U-ser/OneDrive - American University of Phnom Penh/Desktop/image/messi7.jpg",
        "C:/Users/U-ser/OneDrive - American University of Phnom Penh/Desktop/image/messi8.webp",
        "C:/Users/U-ser/OneDrive - American University of Phnom Penh/Desktop/image/messi9.webp",
        "C:/Users/U-ser/OneDrive - American University of Phnom Penh/Desktop/image/messi10.jpg",
        "C:/Users/U-ser/OneDrive - American University of Phnom Penh/Desktop/image/messi11.webp",
        "C:/Users/U-ser/OneDrive - American University of Phnom Penh/Desktop/image/messi12.jpg",
        "C:/Users/U-ser/OneDrive - American University of Phnom Penh/Desktop/image/messi13.webp",
        "C:/Users/U-ser/OneDrive - American University of Phnom Penh/Desktop/image/messi14.jpg",
        "C:/Users/U-ser/OneDrive - American University of Phnom Penh/Desktop/image/messi15.jpg",
        "C:/Users/U-ser/OneDrive - American University of Phnom Penh/Desktop/image/messi16.jpg",
        "C:/Users/U-ser/OneDrive - American University of Phnom Penh/Desktop/image/messi17.jpg",
        "C:/Users/U-ser/OneDrive - American University of Phnom Penh/Desktop/image/messi18.jpg",
        "C:/Users/U-ser/OneDrive - American University of Phnom Penh/Desktop/image/messi19.jpg",
        "C:/Users/U-ser/OneDrive - American University of Phnom Penh/Desktop/image/messi20.jpg",
    ]
    messi_encodings = []
    for image_path in messi_images:
        image = face_recognition.load_image_file(image_path)
        encodings = face_recognition.face_encodings(image)
        if encodings:
            messi_encodings.append(encodings[0])

    # Combine all encodings and names
    known_face_encodings = (
        hour_encodings +
        messi_encodings
    )
    known_face_names = (
        ["Hour"] * len(hour_encodings)+
        ['Messi'] * len(messi_encodings)
    )

    known_face_genders = {
        'Hour': 'Male',
        'Messi' : 'Male'
    }

    return known_face_encodings, known_face_names, known_face_genders
