import cv2

# variables
height = 320
width = 180
FPS = 60
cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)

cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FPS,FPS)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*"MJPG"))

while True:
    ignore,frame = cam.read()
    cv2.imshow("my cam",frame)
    cv2.moveWindow("my cam",0,0)

    if cv2.waitKey(1) & 0xff == ord("q"):
        break
cam.release()
