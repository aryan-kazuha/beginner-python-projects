import cv2

class hand_gesture:
    import mediapipe as mp
    def __init__(self,num_hands=2,tol1=.5,tol2=.5):
        self.hands = self.mp.solutions.hands.Hands(static_image_mode = False,max_num_hands=num_hands,min_detection_confidence=tol1,min_tracking_confidence =tol2)
    def marks(self,frame):
        frameRGB = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        Hands = []
        handType = []
        result = self.hands.process(frameRGB)
        if result.multi_hand_landmarks != None:
            for hand in result.multi_handedness:
                arm = hand.classification[0].label
                handType.append(arm)
            for hand_landmarks in result.multi_hand_landmarks:
                pos = []
                for landmarks in hand_landmarks.landmark:
                    pos.append((int(landmarks.x*width),int(landmarks.y*height)))
                Hands.append(pos)
        return Hands,handType

height = 720
width = 1280
fps = 30
xdelta = 8
ydelta = 8
radius = 10
paddle_color = (0,0,0)
paddle_width = 100
paddle_height = 25
xpos = width//2
ypos = height//2

'''
def ball(xpos,ypos,xdelta,ydelta,height,width):
    if xpos-radius <=0 or xpos+radius>=width:
        xdelta = -xdelta
    if ypos - radius <= 0:
        ydelta = -ydelta
    if ypos + radius >= height:
        ydelta = -abs(ydelta)
    xpos += xdelta
    ypos +=ydelta
    
    return xpos,ypos,xdelta,ydelta
'''
    

cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FPS,fps)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*"MJPG"))

lefthand = hand_gesture()
righthand = hand_gesture()

while True:
    
    ignore,frame = cam.read()
    frame = cv2.flip(frame,1)
    '''
    xpos,ypos,xdelta,ydelta= ball(xpos,ypos,xdelta,ydelta,height,width)
    cv2.circle(frame,(xpos,ypos),radius,(0,0,255),-1)
    '''
    Lhands,LhType = lefthand.marks(frame)
    Rhands,RhType = righthand.marks(frame)

    if LhType != []:
        if LhType[0]== "Left":
            paddle_color = (255,0,0)
            finger_pos = Lhands[0][8]
            cv2.rectangle(frame,(0,finger_pos[1]-paddle_width//2),(paddle_height,finger_pos[1]+paddle_width//2),paddle_color,-1)
    
    if RhType != []:
        if RhType[0]== "Right" :
            paddle_color = (0,0,255)
            finger_pos = Rhands[0][8]
            cv2.rectangle(frame,(0,finger_pos[1]-paddle_width//2),(paddle_height,finger_pos[1]+paddle_width//2),paddle_color,-1)
    cv2.imshow("my cam",frame)
    cv2.moveWindow("my cam",0,0)
    if cv2.waitKey(1) & 0xff == ord("q"):
        break

cam.release()
cv2.destroyAllWindows()