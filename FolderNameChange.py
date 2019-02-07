# -*- coding: utf-8 -*-
import os
import shutil

def change_folder_name(folder_path):

    os.chdir(folder_path)
    dirs = os.listdir(folder_path)
    count = 1

    for folders in dirs:

        new_folder_name = 's' + str(count)
        os.rename(folders, new_folder_name)
        count += 1


def extract_image(folder_path):

    os.chdir(folder_path)
    dirs = os.listdir(folder_path)
    for folders in dirs:
        sub_folder = folder_path + "/" + folders
        sub_folder_name = os.listdir(sub_folder)
        for images in sub_folder_name:
            oldname = sub_folder + "/" + images
            newname = 'C:/Users/kiokh/Desktop/OpenCV/data0' + '/' + images
            shutil.copyfile(oldname, newname)


change_folder_name('C:/Users/kiokh/Desktop/OpenCV/data')
extract_image('C:/Users/kiokh/Desktop/OpenCV/data')

