import picamera
import time


camera = picamera.PiCamera()

camera.resolution = (2592, 1944)
camera.brightness = 65

camera.annotate_text_size=128
camera.annotate_foreground = picamera.Color('black')
camera.annotate_background = picamera.Color('white')
camera.annotate_text = " Syrus "

camera.capture("SyrusLegoIOT.jpg")


