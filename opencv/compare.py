import cv2
import numpy as np

img1 = cv2.imread("images/cat_3.jpg")
img2 = cv2.imread("images/cat_1.jpg")

diff = cv2.subtract(img1, img2)

result = not np.any(diff)

if result:
    print("Images are the same")
else:
    cv2.imwrite("images/result.jpg", diff)
    print("Images are different")

