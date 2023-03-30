import cv2
import numpy as np



inp = cv2.imread("image_examples/Modi.jpg")
resizedImg = cv2.resize(inp,(550,600)) #width x Height
croppedImg = inp[0:200,200:800] # first height 2nd is width

cv2.imshow('Modi Image',inp)
cv2.imshow('Cropped Image',croppedImg)
cv2.imshow("reSized Image",resizedImg)

cv2.waitKey(0)
cv2.destroyAllWindows()

print(inp.shape)
print(f"Height of the image is: {int(inp.shape[0])} pixels")
print(f"Width of the image is: {int(inp.shape[1])} pixels")

cv2.imwrite('output.jpg',inp)
