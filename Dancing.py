import cv2
import cvzone
import numpy as np
import time
import PoseModule as pm
import serial
import mediapipe as mp
import HandTrackingModule as htm
import math
from cvzone.HandTrackingModule import HandDetector


commPort= "COM4"
ser = serial.Serial(commPort, baudrate=115200)

cap = cv2.VideoCapture(0)
detector = pm.poseDetector()
detector2 = htm.handDetector(maxHands=2)


count = 0
dir = 0
pTime = 0

while True:
    success, img = cap.read()
    img = cv2.resize(img, (640, 480))
    # img = cv2.imread("AiTrainer/test.jpg")
    img = detector2.findHands(img)
    img = detector.findPose(img, False)


    lmList = detector.findPosition(img, False)
    lmList2 = detector2.findPosition(img, False)
    #print(lmList)
    if len(lmList) != 0:
        # left Arm1
        angle1 = detector.findAngle(img, 11, 12, 14)
        # left Arm2
        angle2 = detector.findAngle(img, 16, 14, 12)
        # right Arm1
        angle3 = detector.findAngle(img, 13, 11, 12)
        # right Arm2
        angle4 = detector.findAngle(img, 11, 13, 15)

        angle5 = detector.findAngle(img, 23, 25, 27)


        #################1
        if angle1>=260:
            angle1=260
        elif angle1<=260 and angle1>=250:
            angle1=250
        elif angle1<=250 and angle1>=240:
            angle1=240
        elif angle1<=240 and angle1>=230:
            angle1=230
        elif angle1<=230 and angle1>=220:
            angle1=220
        elif angle1 <= 220 and angle1 >= 210:
            angle1 = 210
        elif angle1<=210 and angle1>=200:
            angle1=200
        elif angle1<=200 and angle1>=190:
            angle1=190
        elif angle1<=190 and angle1>=180:
            angle1=180
        elif angle1<=180 and angle1>=170:
            angle1=170
        elif angle1<=170 and angle1>=160:
            angle1=160
        elif angle1 <= 160 and angle1 >= 150:
            angle1 = 150
        elif angle1 <= 150 and angle1 >= 140:
            angle1 = 140
        elif angle1<=140 and angle1>=130:
            angle1=130
        elif angle1<=130 and angle1>=120:
            angle1=120
        elif angle1<=120 and angle1>=110:
            angle1=110
        elif angle1<=110 and angle1>=100:
            angle1=100
        elif angle1<=100:
            angle1=90
        #######################
        if angle2 >=260:
            angle2=-90
        elif angle2 <= 260 and angle2 >= 250:
            angle2 = -80
        elif angle2 <= 250 and angle2 >= 240:
            angle2 = -70
        elif angle2 <= 240 and angle2 >= 230:
            angle2 = -60
        elif angle2 <= 230 and angle2 >= 220:
            angle2 = -50
        elif angle2 <= 220 and angle2 >= 210:
            angle2 = -40
        elif angle2 <= 210 and angle2 >= 200:
            angle2 = -30
        elif angle2 <= 200 and angle2 >= 190:
            angle2 = -20
        elif angle2 <= 190 and angle2 >= 180:
            angle2 = -10
        elif angle2<=180 and angle2>=170:
            angle2=0
        elif angle2<=170 and angle2>=160:
            angle2=10
        elif angle2 <= 160 and angle2 >= 150:
            angle2 = 20
        elif angle2 <= 150 and angle2 >= 140:
            angle2 = 130
        elif angle2<=140 and angle2>=130:
            angle2=40
        elif angle2<=130 and angle2>=120:
            angle2=50
        elif angle2<=120 and angle2>=110:
            angle2=60
        elif angle2<=110 and angle2>=100:
            angle2=70
        elif angle2<=100 and angle2>=90:
            angle2=80
        elif  angle2 <= 90:
            angle2 = 90
        ####################3
        if angle3 >= 260:
            angle3 = 260
        elif angle3 <= 260 and angle3 >= 250:
            angle3 = 250
        elif angle3 <= 250 and angle3 >= 240:
            angle3 = 240
        elif angle3 <= 240 and angle3 >= 230:
            angle3 = 230
        elif angle3 <= 230 and angle3 >= 220:
            angle3 = 220
        elif angle3 <= 220 and angle3 >= 210:
            angle3 = 210
        elif angle3 <= 210 and angle3 >= 200:
            angle3 = 200
        elif angle3 <= 200 and angle3 >= 190:
            angle1 = 190
        elif angle3 <= 190 and angle3 >= 180:
            angle3 = 180
        elif angle3<=180 and angle3>=170:
            angle3=170
        elif angle3<=170 and angle3>=160:
            angle3=160
        elif angle3 <= 160 and angle3 >= 150:
            angle3 = 150
        elif angle3 <= 150 and angle3 >= 140:
            angle3 = 140
        elif angle3<=140 and angle3>=130:
            angle3=130
        elif angle3<=130 and angle3>=120:
            angle3=120
        elif angle3<=120 and angle3>=110:
            angle3=110
        elif angle3<=110 and angle3>=100:
            angle3=100
        elif angle3<=100:
            angle3=90
        ######################4
        if angle4 >= 260:
            angle4 = -90
        elif angle4 <= 260 and angle4 >= 250:
            angle4 = -80
        elif angle4 <= 250 and angle4 >= 240:
            angle4 = -70
        elif angle4 <= 240 and angle4 >= 230:
            angle4 = -60
        elif angle4 <= 230 and angle4 >= 220:
            angle4 = -50
        elif angle4 <= 220 and angle4 >= 210:
            angle4 = -40
        elif angle4 <= 210 and angle4 >= 200:
            angle4 = -30
        elif angle4 <= 200 and angle4 >= 190:
            angle4 = -20
        elif angle4 <= 190 and angle4 >= 180:
            angle4 = -10
        elif angle4 <= 180 and angle4 >= 170:
            angle4 = 0
        elif angle4 <= 170 and angle4 >= 160:
            angle4 = 10
        elif angle4 <= 160 and angle4 >= 150:
            angle4 = 20
        elif angle4 <= 150 and angle4 >= 140:
            angle4 = 130
        elif angle4 <= 140 and angle4 >= 130:
            angle4 = 40
        elif angle4 <= 130 and angle4 >= 120:
            angle4 = 50
        elif angle4 <= 120 and angle4 >= 110:
            angle4 = 60
        elif angle4 <= 110 and angle4 >= 100:
            angle4 = 70
        elif angle4 <= 100 and angle4 >= 90:
            angle4 = 80
        elif angle4 <= 90:
            angle4 = 90

        if angle5 <= 220 and angle5 >= 150:
            angle5 = 0
        elif angle5 >=220:
            angle5 = 30
        elif angle5 <=150:
            angle5 = -30


    if len(lmList2) !=0:

        #print(lmList2[4], lmList2[8])

        x1, y1= lmList2[4][1], lmList2[4][2]
        x2, y2 = lmList2[8][1], lmList2[8][2]
        cx,cy=(x1+x2)//2, (y1+y2)//2

        cv2.circle(img, (x1,y1), 15, (255,0,255), cv2.FILLED)
        cv2.circle(img, (x2, y2), 15, (255,0,255), cv2.FILLED)
        cv2.line(img,(x1,y1),(x2,y2), (255,0,255),3)
        cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)

        length=math.hypot(x2-x1,y2-y1)
        if length<50:
            cv2.circle(img, (cx,cy),15,(0,255,0), cv2.FILLED)
            length=0
        else:
            length=90

    List=[(angle1-90),angle2,(angle3-90),angle4,angle5]

    entry_list = ''
    for entries in List:
        entry_list = entry_list + str(entries) + ','
        # my_label1.config(text=entry_list)
    msg = entry_list.encode()
    ser.write(msg)
    print(msg)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (50, 100), cv2.FONT_HERSHEY_PLAIN, 5,
                (255, 0, 0), 5)
    cv2.imshow("Image", img)
    cv2.waitKey(1)
    time.sleep(5)