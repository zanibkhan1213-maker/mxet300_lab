import L2_compass_heading as com
import L1_log as log
import time

#cardinal direction 


def card(head):

        if 0 <= head <= 22.5:
            x = "North"

        elif 22.5 < head <= 67.5:
            x = "NorthWest"

        elif 67.5 < head <= 112.5:
            x = "West"

        elif 112.5 < head <= 157.5:
            x = "SouthWest"      

        elif 157.5 < head <= 180:
            x = "South"

        elif -180 <= head < -157.5:
            x = "South"    

        elif -22.5 <= head <= 0:
            x = "North"

        elif -67.5 <= head < -22.5 :
            x = "NorthEast"

        elif -112.5 <= head < -67.5:
            x = "East"

        elif -157.5 <= head < -112.5:
            x = "SouthEast"  

        return x

while(1):
    head = com.get_heading()
    cardinal = card(head)
    log.tmpFile (head, "newfile2.txt") 
    log.stringTmpFile(cardinal, "newfile3.txt") 
    time.sleep(0.2)


    
       


  