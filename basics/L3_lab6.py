import L1_log as log
import L1_lidar as lidar
import L2_vector as vec
import math as mth
from time import sleep
sensor = lidar.Lidar()
sensor.connect()
sensor.run()
sleep(2) # let the first scan arrive

while True:
    # get a scan from the sensor
    lscan = sensor.get()

    # find the nearest obstacle in that scan
    obstacle = vec.getNearest(lscan)

    distance = obstacle[0]
    angle = obstacle[1]

    #x coordinate
    x = distance * mth.sin(angle)

    #y coordinate
    y = distance * mth.cos(angle)

    # write the distance to its own file
    log.tmpFile(distance, "distance.txt")
    
    # write the angle to its own file
    log.tmpFile(angle, "angle.txt")

    log.tmpFile(x, "x.txt")
    log.tmpFile(y, "y.txt")

    # sleep
    sleep(0.2)