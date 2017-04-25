from picamera import PiCamera
import subprocess
import time

c = PiCamera()
c.rotation = 180

c.resolution = (1280,720)

start = time.time()
pictime = time.time()

for i in [1,2,3,4]:
    print("{:d} picture".format(i))
    c.capture( "testr{:d}.jpg".format(i) )
    print("took {:f} sec".format(time.time() - pictime))
    pictime = time.time()

print("took {:f} sec to take 4 pictures".format(time.time() - start))

start = time.time()
subprocess.call("convert testr1.jpg testr2.jpg testr3.jpg testr4.jpg -append out-rot.jpg",shell=True)
print("took {:f} seconds to convert".format(time.time() - start))

