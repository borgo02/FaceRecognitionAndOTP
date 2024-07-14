#!/usr/bin/env python3
import serial
import cv2
import pickle
import requests
from PIL import Image
import numpy as np
import os
import subprocess
import time
#import docker


otp = 0
status = 0
#Status =   0   idle
#           1   ultrasuoni attivo    
#           2   volto riconosciuto
#           3   otp corretto
#           4   otp errato --> poi ripasso in 2

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(BASE_DIR, "images")

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainer4.yml")

labels = {}
with open("labels4.pickle", "rb") as f:
    og_labels = pickle.load(f)
    labels = {v:k for k,v in og_labels.items()}

def face_recognition():
    tentative = 0
    while(True):
        path = os.path.join(BASE_DIR, "test1.jpg")
        #client = docker.from_env()
        volume_bindings = {
        '/app': {'bind': '/shared', 'mode': 'rw'}
        }
        #container = client.containers.run("test_docker_v15",
        #                                volumes=volume_bindings,
        #                                privileged=True,
        #                                detach=True)
        #exit_code = container.wait()
        #print(exit_code)
        #for i in range (1, 6):
        #    time.sleep(1)
        #    print(i)
        subprocess.run(["fswebcam %s"%(path)], shell=True)
        time.sleep(3)
        error = True
        while error:
            try:
                #normal =  Image.open("/shared/test.jpg")
                normal = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
                normal = cv2.resize(normal, (250, 250))

                error = False
            except:
                error = True
                time.sleep(3)
        if normal is not None:
            #gray =  normal.convert("L")
            #image_array = np.array(gray, "uint8")
            id_, conf = recognizer.predict(normal)
            if(conf>=70 and conf <=120):
                return True
            else:
                tentative = tentative + 1
                print('Non riconosciuto')
            
            if (tentative > 3):
                return False


if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.reset_input_buffer()

    line = ""
    while True:
        if ser.in_waiting > 0:
#           draft_line = ser.readline().decode('ascii').rstrip()
            draft_line = ""
            isReading=True
            while isReading:
                if ser.in_waiting > 0:
                    draft_line += ser.read(ser.in_waiting).decode('ascii')
                    if '\n' in draft_line:
                        isReading=False
            print(draft_line)
            if draft_line != "":
                splitted_line = draft_line.split(':')
                if splitted_line[0] == "s":
                    status = int(splitted_line[1])
                elif splitted_line[0] == "o":
                    otp = int(splitted_line[1])
        

        if status != 0:
            if status == 1:
                recog_status = face_recognition()
                print(recog_status)
                if recog_status:
                    stringToSend = "stato_1\n"
                    try:
                        ser.write(stringToSend.encode('ascii'))
                    except Exception as error:
                        print(error)
                    status = 2
                else:
                    stringToSend = "stato_0\n"
                    try:
                        ser.write(stringToSend.encode('ascii'))
                    except Exception as error:
                        print(error)
                    status = 0
            elif status == 2:
                if otp != 0:
                    r = requests.get(f'https://pyotp-service.azurewebsites.net/api/http_trigger?code={otp}')
                    if "True" in r.text[0:1000]:
                        status = 3
                    else: 
                        status = 4
                    otp = 0
            elif status == 3:
                #di arduino di accendere led
                stringToSend = "stato_3\n"
                ser.write(stringToSend.encode('ascii'))
                status = 0
            elif status == 4:
                #scrivi ad arduino di tornare ad inserire il codice
                stringToSend = "stato_4\n"
                ser.write(stringToSend.encode('ascii'))
                status = 2