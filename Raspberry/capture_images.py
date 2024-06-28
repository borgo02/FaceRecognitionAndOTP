#from picamera import PiCamera
from time import sleep
import subprocess
from datetime import datetime
import os
#import docker

#camera = PiCamera()

#camera.start_preview()
#sleep(5)
#camera.stop_preview()

filename = "test.jpg"

#client = docker.from_env()
#container = client.containers.run("test_docker_v14", detach=True)
#print("Saving container to %s"%(container))
subprocess.run(["fswebcam %s"%(filename)], shell=True)
print("Saving photo to %s"%(filename))

#time.sleep(10)