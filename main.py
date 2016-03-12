from SimpleCV import Camera, Image
import indicoio
import pyglet
import numpy
import os

indicoio.config.api_key = 'b16ad77cb57fc7a13730412d3daeff9e'

cam = Camera()
image = cam.getImage()

temp = "image.jpg"
image.save(temp)

emotions = indicoio.fer(temp)

print max(emotions, key=emotions.get)
print emotions

os.remove(temp)
