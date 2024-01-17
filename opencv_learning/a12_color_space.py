import cv2

def main():
    cap = cv2.VideoCapture(0)
    con = True
    while con:
        ret, frame = cap.read()
        # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        h, s, v = cv2.split(frame)
        # filtering hue channel
        h = cv2.inRange(h, 0, 50) 
        frame = cv2.merge((h, s, v))
        frame = cv2.cvtColor(frame, cv2.COLOR_HSV2BGR)
        if ret:
            cv2.imshow("frame", frame)
        if cv2.waitKey(1) == ord("q"):
                con = False



if __name__ == "__main__":
    main()