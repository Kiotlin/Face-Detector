# -*- coding: utf-8 -*-
import cv2
import os
import numpy as np
from FaceDetect import face_detect
from DataPrepare import prepare_training_data


# draw rectangle on image
def draw_rectangle(img, rect):

    if rect is not None:
        (x, y, w, h) = rect
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
        print('success')
        return 1
    else:
        print('fail')
        return 0


def detect_face(test_img):
    img = test_img.copy()
    face, rect = face_detect(img)

    # label = face_recognizer.predict(face)
    # print(label)
    draw_rectangle(img, rect)
    return img


def accuracy_compute():
    count = 0
    base_dir = "data0"
    dirs = os.listdir(base_dir)
    for images in dirs:
        images_path = base_dir + "/" + images
        img_face = cv2.imread(images_path)
        face, rect = face_detect(img_face)
        detected_img_face = draw_rectangle(img_face, rect)
        if detected_img_face == 1:
                count += 1
    print("Total face statistics: 1054")
    print("Successfully detected face statistics: " + str(count))
    accuracy = float(count / 1054)
    print("Accuracy: " + str(accuracy * 100) + "%")


# # start reading face images
# print('Preparing data')
# faces, labels = prepare_training_data('data')
# print('Data prepared')

# # print total faces and labels
# print('Total faces: ', len(faces))
# print('Total labels: ', len(labels))

# # ------ create face recognizer ------
# face_recognizer = cv2.face.createLBPHFaceRecognizer()
# face_recognizer.train(faces, np.array(labels))

# # ------ detect human faces -------
print('Roger on detecting face...')
# face_path = 'origin_data/Aaron_Guiel/Aaron_Guiel_0001.jpg'
# test_face = cv2.imread(face_path)
# detected_faces = detect_face(test_face)
# cv2.namedWindow('result', cv2.WINDOW_AUTOSIZE)
# cv2.imshow('result', detected_faces)
# c = cv2.waitKey(0)
# if c == 27:
#     cv2.destroyAllWindows()
accuracy_compute()