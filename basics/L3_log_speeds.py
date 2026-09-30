import time
import L2_kinematics as k
import L1_log as log



while True:
    cspeed = k.getMotion() #xdot, theta dot

    xdot = cspeed[0]
    thetadot = cspeed[1]

    wspeed = k.pdCurrents #pdl, pdr

    pdl = wspeed[0]
    pdr = wspeed[1]
    print("xdot: ", xdot, "thetadot: ", thetadot, "pdlg: ", pdl, "pdr: ", pdr)
    log.tmpFile (xdot, "newfile.txt")
    log.tmpFile (thetadot, "newfile2.txt")
    log.tmpFile (pdl, "newfile3.txt")
    log.tmpFile (pdr, "newfile4.txt")

    time.sleep(0.2)