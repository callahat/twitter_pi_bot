import subprocess

IMG_WIDTH = 1280
IMG_HEIGHT = 720
ROTATE = 180

# this is the command to capture the image using pi camera
snapCommand = "raspistill -rot {:d} -w {:d} -h {:d}".format(ROTATE, IMG_WIDTH, IMG_HEIGHT)

def captureImage(filepath):
    ret = subprocess.call(snapCommand + " -o " + filepath, shell=True)
