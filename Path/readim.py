import numpy as np
import cv2

img = cv2.imread("C:\\Users\\admin\\Desktop\\3FO4JPJWICI9.png", cv2.IMREAD_GRAYSCALE)

# cv2.namedWindow("Image")
# cv2.imshow("Image", img)
# cv2.waitKey(0)
# cv2.destoryAllWindows()

print(img[3][4])
a = img.shape
print(a)