import cv2
import numpy as np

image1 = cv2.imread("cat_1.jpg")
image2 = cv2.imread("cat_2.jpg")

difference = cv2.subtract(image1, image2)

result = not np.any(difference)

if result == True:
    print ("The images are the same")
else:
    cv2.imwrite("result.jpg", difference)
    print("The images are different")
