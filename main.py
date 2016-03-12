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
os.remove(temp)

mood = max(emotions, key=emotions.get)
songPath = "music/"
songPath += mood + "/"


for (dirpath, dirnames, filenames) in os.walk(songPath):
	songPath += filenames[0]
	break

print songPath

song = pyglet.media.load(songPath)
song.play()
pyglet.app.run()
