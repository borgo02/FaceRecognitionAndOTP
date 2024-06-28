#from picamera import PiCamera
from time import sleep
import subprocess
from datetime import datetime
import os

#camera = PiCamera()

#camera.start_preview()
#sleep(5)
#camera.stop_preview()

filename = "test.jpg"

subprocess.run(["fswebcam %s"%(filename)], shell=True)

print("Saving photo to %s"%(filename))

#time.sleep(10)