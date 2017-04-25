import subprocess

IMG_WIDTH = "1280"
IMG_HEIGHT = "720"
IMG_NAME = "tweet-pic.jpg"
ROTATE = "180"

snapCommand = "raspistill -rot " + ROTATE +  " -w " + IMG_WIDTH +  " -h " + IMG_HEIGHT
# snapCommand = "raspistill -w " + IMG_WIDTH +  " -h " + IMG_HEIGHT

start = time.time()
pictime = time.time()

for i in [1,2,3,4]:
    print("{:d} picture".format(i))
    subprocess.call(snapCommand + " -o testr{:d}.jpg".format(i), shell=True) 
    print("took {:f} sec".format(time.time() - pictime))
    pictime = time.time()

print("took {:f} sec to take 4 pictures".format(time.time() - start))

start = time.time()
subprocess.call("convert testr1.jpg testr2.jpg testr3.jpg testr4.jpg -append out-rot.jpg",shell=True)
print("took {:f} seconds to convert".format(time.time() - start))

