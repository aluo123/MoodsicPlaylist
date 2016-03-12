from SimpleCV import Image, Camera

cam = Camera()
img = cam.getImage()
img.save("helloworld.jpg")
