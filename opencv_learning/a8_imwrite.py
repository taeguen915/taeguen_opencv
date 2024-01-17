import cv2


def main():
    img = cv2.imread("/home/uav402/taeguen_opencv/opencv_learning/data/lena.jpg", 1)

    cv2.imwrite("/home/uav402/taeguen_opencv/opencv_learning/output/lena_copy.png", img)

    cv2.imwrite("/home/uav402/taeguen_opencv/opencv_learning/output/lena_copy.bmp", img)

    cv2.imwrite("/home/uav402/taeguen_opencv/opencv_learning/output/lena_copy.jpg", img, [cv2.IMWRITE_JPEG_QUALITY, 8])
    
    cv2.imwrite("/home/uav402/taeguen_opencv/opencv_learning/output/lena_copy1.jpg", img, [cv2.IMWRITE_JPEG_QUALITY, 50])
   


if __name__ == "__main__":
    main()