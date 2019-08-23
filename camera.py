import sys
import cv2
import datetime
import os, sys

def setting():
    """
    カメラモジュールの読み込み
    """
    cap = cv2.VideoCapture("/dev/video1")
    if not cap.isOpened():
        return -1
    else:
        return cap

def getTimestamp():
    """
    現在時刻の文字列生成を生成するファンクション
    """
    dt_now = datetime.datetime.now()
    dt = dt_now.strftime("%Y%m%d%H%M%S")

    return dt

def shoot(cap):
    """
    写真を撮影するファンクション
    """

    filename = getTimestamp() + ".jpg"
    path = "/home/nvidia/Pictures/" + filename 
    
    ret_val, img = cap.read()
    crop_img = img[80:480, 120:520]
    cv2.imwrite(path,crop_img)
    cap.release()
    return filename

if __name__ == '__main__':
    cap = setting()
    shoot(cap)

