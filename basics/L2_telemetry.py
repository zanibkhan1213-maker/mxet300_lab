import L1_log as log
import L1_ina as vol
import time

#Voltage Reading from L1_ina
while(1):
    Voltage = vol.readVolts()
    log.tmpFile (Voltage, "newfile.txt")
    time.sleep(0.2)