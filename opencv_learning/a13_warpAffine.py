import cv2

def main():
    cap = cv2.VideoCapture(0)
    con = True
    M1 = cv2.getRotationMatrix2D((0, 0), 45, 1)
    M1[0][2] += 200
    M1[1][2] += 200
    while con:
        ret, frame = cap.read()
        if ret:
            frame = cv2.warpAffine(frame, M1, (frame.shape[1],frame.shape[0]))
            cv2.imshow("frame", frame)
        if cv2.waitKey(1) == ord("q"):
                con = False



if __name__ == "__main__":
    main()