import cv2
from matplotlib import pyplot as plt

def main():
    imgRBG = cv2.imread("/home/uav402/taeguen_opencv/opencv_learning/data/lena.jpg", 1)

    b, g, r = cv2.split(imgRBG)
    imgRBS = cv2.merge((r,g,b))
    plt.axis('off')
    plt.imshow(imgRBG)
    # plt.imshow(r)
    plt.show()
       
    cv2.imshow("lena", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()