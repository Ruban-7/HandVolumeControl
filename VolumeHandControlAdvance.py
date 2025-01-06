import cv2
import time
import numpy as np
import math
import SampleHandTrackingModule as htm
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

wCam, hCam = 640, 480
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0

detector = htm.handDetector(detectionCon=0.7,maxHands=1)


devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)
volRange=volume.GetVolumeRange()

minVol=volRange[0]
maxVol=volRange[1]
vol=0
volBar=400
volPer=0
area=0
colorVol=(255,0,0)
while True:
    success, img = cap.read()
    #Find Hand
    img = detector.findHands(img)
    lmlist, bbox = detector.findPosition(img, draw=True)
    if len(lmlist) > 12:  # Check if the required landmarks are detected
        # Filter based on size
        area =(bbox[2]-bbox[0])*(bbox[3]-bbox[1])//100
        #print(area)
        if 250<area<1000:
            #print("yes")


            #find distance between Index and Thumb
            length, img, lineInfo = detector.findDistance(4, 8, img)
            #print(length)

            #convert Volume
            #Hand Range 50-300
            ##Volume Range -65 - 0
            #vol = np.interp(length, [50, 300], [minVol, maxVol])
            volBar = np.interp(length, [50, 200], [400, 150])
            volPer = np.interp(length, [50, 200], [0, 100])
            #volume.SetMasterVolumeLevel(vol, None)

            # print(vol)

            #reduce resolution to make it smoother
            smoothness =10
            volPer= smoothness * round (volPer/smoothness)

            # check fingers up
            fingers=detector.fingersUp()
            #print(fingers)

            #if pinky is down set volume
            if not fingers[4]:
                volume.SetMasterVolumeLevelScalar(volPer / 100, None)
                cv2.circle(img, (lineInfo[4], lineInfo[5]), 15, (0, 255, 0), cv2.FILLED)
                colorVol=(0,255,0)
                time.sleep = (0.25)
            else:
                colorVol=(255,0,0)
            #drawings



            #print(lmlist[4], lmlist[8])

            #print(length)


    else:
        print("Insufficient landmarks detected.")
    cv2.rectangle(img,(50,150),(85,400),(0,255,0),3)
    cv2.rectangle(img,(50, int(volBar)), (85, 400), (0, 255, 0), cv2.FILLED)
    cv2.putText(img, f'{int(volPer)}%', (40, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 3)
    cVol=int(volume.GetMasterVolumeLevelScalar()*100)
    cv2.putText(img, f'Vol Set:{int(cVol)}', (400, 50), cv2.FONT_HERSHEY_COMPLEX, 1, colorVol, 3)
    # frame rate
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (40, 40), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 3)
    cv2.imshow("Img", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit
        break
