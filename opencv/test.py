import cv2
img = cv2.imread("cat_1.jpg")
img = cv2.resize(img, (0, 0), fx=2, fy=2)
img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
cv2.imwrite("cat_new.jpg", img)

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()