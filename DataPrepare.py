# -*- coding: utf-8 -*-
import cv2
import os
from FaceDetect import face_detect


def prepare_training_data(data_folder_path):

    # Get data path details
    dirs = os.listdir(data_folder_path)

    # List to save all faces
    faces = []

    # List to save all labels
    labels = []

    for dir_name in dirs:

        # Our subject directory starts with 's'
        # if have, ignore any unrelated directories
        if not dir_name.startswith("s"):
            continue

        # Extract label number from dir_name
        # directory format => s'label'
        label = int(dir_name.replace("s", ""))

        # sample subject_dir_path = "training-data/s1"
        subject_dir_path = data_folder_path + "/" + dir_name

        # Get image names
        subject_images_names = os.listdir(subject_dir_path)

        # read images
        # detect faces & add faces into list
        for image_name in subject_images_names:

            # ignore system files like .DS_Store
            if image_name.startswith("."):
                continue

            # create image path
            # sample image path = training-data/s1/1.png
            image_path = subject_dir_path + "/" + image_name

            # read image
            image = cv2.imread(image_path)

            # Show image windows to show images
            cv2.namedWindow("Training on image...", cv2.WINDOW_NORMAL)
            cv2.imshow("Training on image...", image)
            cv2.waitKey(100)

            # Detect faces
            face, rect = face_detect(image)

            # ignore undetected faces
            if face is not None:
                # add face to face list
                faces.append(face)
                # add face with label
                labels.append(label)

    cv2.destroyAllWindows()
    cv2.waitKey(1)
    cv2.destroyAllWindows()

    return faces, labels



