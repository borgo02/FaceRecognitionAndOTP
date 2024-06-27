#!/usr/bin/env python3
import serial
import cv2
import pickle
import requests

otp = 0
status = 1
#Status =   0   idle
#           1   ultrasuoni attivo    
#           2   volto riconosciuto
#           3   otp corretto
#           4   otp errato --> poi ripasso in 2



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
        #capture frame-by-frame
        ret, frame = cap.read()
        if frame is not None:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
            for(x, y, w, h) in faces:
                print(x, y, w, h)
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = frame[y:y+h, x:x+w]

                #recognize deep learned model predict 
                id_, conf = recognizer.predict(roi_gray)
                if(conf>=75):
                    print(id_)
                    print(labels[id_])
                    print(conf)
                    return True

                img_item = "my-image.png"
                cv2.imwrite(img_item, roi_gray)

                color = (255, 0, 0)  #BGR 0-255
                stroke = 2
                end_cord_x = x + w
                end_cord_y = y + h
                cv2.rectangle(frame, (x, y), (end_cord_x, end_cord_y), color, stroke)

            cv2.imshow("Frame",frame)

            #display the resulting frame
            #cv2.imshow('frame', frame)
            if cv2.waitKey(20) & 0xFF == ord('q'):
                break


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