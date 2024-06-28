#!/usr/bin/env python3
import serial
import cv2
import pickle
import requests
from PIL import Image
import numpy as np
import os
import subprocess

otp = 0
status = 1
#Status =   0   idle
#           1   ultrasuoni attivo    
#           2   volto riconosciuto
#           3   otp corretto
#           4   otp errato --> poi ripasso in 2

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(BASE_DIR, "images")

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainer.yml")

cap = cv2.VideoCapture(0)

labels = {}
with open("labels.pickle", "rb") as f:
    og_labels = pickle.load(f)
    labels = {v:k for k,v in og_labels.items()}

def face_recognition():
    while(True):
        path = os.path.join(BASE_DIR, "test.jpg")
        subprocess.run(["sudo fswebcam %s"%(path)], shell=True)
        #subprocess.Popen("sudo fswebcam image.jpg",shell=True).communicate()
        normal =  Image.open(path)
        if normal is not None:
            gray =  normal.convert("L")
            image_array = np.array(gray, "uint8")
            id_, conf = recognizer.predict(image_array)
            if(conf>=75):
                print(id_)
                print(labels[id_])
                print(conf)
                return True


if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.reset_input_buffer()

    line = ""
    while True:
        if ser.in_waiting > 0:
            draft_line = ser.readline().decode('utf-8').rstrip()
            print(draft_line + "asd")
            if draft_line != "":
                splitted_line = draft_line.split(':')
                if splitted_line[0] == "s":
                    status = int(splitted_line[1])
                elif splitted_line[0] == "o":
                    otp = int(splitted_line[1])
            print(status)
            print(otp)
            if status == 1:
                recog_status = face_recognition()
                if recog_status:
                    stringToSend = "stato_1"
                    ser.write(stringToSend.encode('utf-8'))
                    status = 2
                break
            elif status == 2:
                if otp != 0:
                    r = requests.get(f'https://pyotp-service.azurewebsites.net/api/http_trigger?code={otp}')
                    if "True" in r.text[0:1000]:
                        status = 3
                    else: 
                        status = 4
                    otp = 0
                break
            elif status == 3:
                #di arduino di accendere led
                stringToSend = "stato_3"
                ser.write(stringToSend.encode('utf-8'))
                status = 0
                break
            elif status == 4:
                #scrivi ad arduino di tornare ad inserire il codice
                stringToSend = "stato_4"
                ser.write(stringToSend.encode('utf-8'))
                status = 2
                break       