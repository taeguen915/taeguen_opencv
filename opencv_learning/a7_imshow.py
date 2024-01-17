import cv2

def main():
    img = cv2.imread("lena.jpp", 1)
    cv2.imshow("lena",img)