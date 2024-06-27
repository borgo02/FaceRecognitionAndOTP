#from picamera import PiCamera
from time import sleep
import subprocess
from datetime import datetime
import os

#camera = PiCamera()

#camera.start_preview()
#sleep(5)
#camera.stop_preview()

lapse_dir = datetime.strftime(datetime.now(),"timelapse_%Y%m%d-%H%M%S")
subprocess.call(['mkdir',lapse_dir])

prefix = datetime.strftime(datetime.now(),"%Y%m%d-%H%M%S")
filename = lapse_dir+"/"+prefix+".jpg"

subprocess.call(['fswebcam','-r','350x350','--no-banner',filename])

print("Saving photo to %s"%(filename))

#time.sleep(10)