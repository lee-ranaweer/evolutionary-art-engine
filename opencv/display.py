import matplotlib.pyplot as plt
import cv2
from mse import mse

# Visual plot of difference between images
def display(img1_path, img2_path):
    img1 = cv2.imread(img1_path)
    img2 = cv2.imread(img2_path)

    # Check if images are loaded successfully
    if img1 is None or img2 is None:
        print(f"Error loading images: {img1_path} or {img2_path}")
        return

    # Mean squared error
    error = mse(img1, img2)

    print(f"MSE: {error:.2f}")

    # Absolute difference image
    diff_image = cv2.absdiff(img1, img2)

    plt.figure(figsize=(15, 10))

    # Display image 1
    plt.subplot(2, 2, 1)
    plt.title("Image 1")
    plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
    plt.axis('off')

    # Display image 2
    plt.subplot(2, 2, 2)
    plt.title("Image 2")
    plt.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
    plt.axis('off')

    # Display difference image
    plt.subplot(2, 2, (3, 4))
    plt.title(f'Difference Image\nMSE: {error:.2f}')
    plt.imshow(cv2.cvtColor(diff_image, cv2.COLOR_BGR2RGB))
    plt.axis('off')

    plt.tight_layout()
    plt.show()
