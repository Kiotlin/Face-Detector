

# -*- coding: utf-8 -*-
import cv2


def face_detect(src):
    # Convert image to gray-scale
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

    # Load OpenCV face detector
    # I use Haar classifier
    classifier_path = "haarcascade_frontalface_alt.xml"
    face_detector = cv2.CascadeClassifier(classifier_path)

    # Detect multi-scale images
    faces = face_detector.detectMultiScale(gray, 1.1, 4)

    # If do not detect faces, return original image
    if len(faces) == 0:
        return None, None

    (x, y, w, h) = faces[0]

    # Return only the front part of the image
    return gray[y:y+w, x:x+h], faces[0]






