import cv2
import numpy as np
import matplotlib.pyplot as plt

img1 = cv2.imread('images/panda_1.jpg')
img2 = cv2.imread('images/panda_2.jpg')
img3 = cv2.imread('images/panda_3.jpg')
# img3 = cv2.imread('images/motorcycle.jpg')

# img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
# img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
# img3 = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)

h, w = img1.shape

def mse(img1, img2):
    diff = cv2.subtract(img1, img2)
    err = np.sum(diff**2)
    mse = err/(float(h*w))
    return mse, diff

    # err = np.sum((img1.astype("float") - img2.astype("float")) ** 2)
    # mse = err / (h * w)
    # diff = np.abs(img1 - img2)
    # return mse, diff

match_error12, diff12 = mse(img1, img2)
match_error13, diff13 = mse(img1, img3)
match_error23, diff23 = mse(img2, img3)

print("MSE between img1 and img2:", match_error12)
print("MSE between img1 and img3:", match_error13)
print("MSE between img2 and img3:", match_error23)

plt.subplot(221), plt.imshow(diff12, 'gray'),plt.title("Image1 - Image2"),plt.axis('off')
plt.subplot(222), plt.imshow(diff13, 'gray'),plt.title("Image1 - Image3"),plt.axis('off')
plt.subplot(223), plt.imshow(diff23, 'gray'),plt.title("Image2 - Image3"),plt.axis('off')
plt.show()

# cv2.imshow("Contour", diff12)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# cv2.imshow("Contour", diff13)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# cv2.imshow("Contour", diff23)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# MSE general algorithm
# sum = 0.0
# for(x = 0; x < width;++x){
#    for(y = 0; y < height; ++y){
#       difference = (A[x,y] - B[x,y])
#       sum = sum + difference*difference
#    }
# }
# mse = sum /(width*height)
# printf("The mean square error is %f\n",mse)