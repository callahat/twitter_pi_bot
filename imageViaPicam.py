from picamera import PiCamera

IMG_WIDTH = 1280
IMG_HEIGHT = 720
ROTATE = 180

c = PiCamera()
c.resolution = (IMG_WIDTH, IMG_HEIGHT)
c.rotation = ROTATE

def captureImage(filepath):
    c.capture( filepath )
