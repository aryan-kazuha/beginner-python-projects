import cv2
import time

height = 480
width = 640
fps = 30
u_pos = (440,40)
l_pos = (600,80)
cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FPS,fps)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*"MJPG"))

while True:
    start_time = time.time()
    ignore,frame= cam.read()
    final_time = time.time()
    fps_time = final_time - start_time
    TEXT = int(1.0/fps_time)
    text_1 = "FPS: " + str(TEXT)
    cv2.rectangle(frame,u_pos,l_pos,(0,0,0),1)
    cv2.putText(frame,text_1,(450,70),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0),1)  
    cv2.imshow("my cam",frame)
    if cv2.waitKey(1) & 0xff == ord("q"):
        break