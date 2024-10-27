import numpy as np

# Compute the squared differences for each pixel
def mse(imageA, imageB):
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    # Normalize by total number of pixels
    err /= float(imageA.shape[0] * imageA.shape[1] * imageA.shape[2])
    return err

# sum = 0.0
# for(x = 0; x < width;++x){
#    for(y = 0; y < height; ++y){
#       difference = (A[x,y] - B[x,y])
#       sum = sum + difference*difference
#    }
# }
# mse = sum /(width*height*channels)