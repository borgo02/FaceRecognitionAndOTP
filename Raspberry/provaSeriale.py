#!/usr/bin/env python3
import serial

status = 0
#Status =   0   idle
#           1   ultrasuoni attivo    
#           2   volto riconosciuto
#           3   otp corretto
#           4   otp errato --> poi ripasso in 2

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.reset_input_buffer()

    line = ""
    while True:
        if status == 1:
            if ser.in_waiting > 0:
                line = ser.readline().decode('utf-8').rstrip()
                print(line)
            break
        elif status == 2:
            break
        elif status == 3:
            break
        elif status == 4:
            break
        
        if line != "":
            splitted_line = line
            if splitted_line == "s":
                break
            elif splitted_line == "o":
                break
            elif splitted_line == "i":
                break
        