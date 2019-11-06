import cv2 as cv
import numpy as np
from functions import plot

####
### Thresholding
####

# src_img = cv.imread("img_numbers.png")
# gray_img = cv.cvtColor(src_img, cv.COLOR_BGR2GRAY)
# limit =
# max_value =
#
# val, thresh_img =
#
# cv.imshow("Original Image", gray_img)
# cv.imshow("Thresholding Example", thresh_img)
#
# cv.waitKey(0)
# cv.destroyAllWindows()

####
### Tipos diferentes de thresholding
####

# src_img = cv.imread("linear_gradient.png")
# gray_img = cv.cvtColor(src_img, cv.COLOR_BGR2GRAY)
#
# limit = 127
# max_value = 255
#
# val, thresh1 = cv.threshold(gray_img, limit, max_value, )
# val, thresh2 = cv.threshold(gray_img, limit, max_value, )
# val, thresh3 = cv.threshold(gray_img, limit, max_value, )
# val, thresh4 = cv.threshold(gray_img, limit, max_value, )
# val, thresh5 = cv.threshold(gray_img, limit, max_value, )
#
# titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
# images = [gray_img, thresh1, thresh2, thresh3, thresh4, thresh5]
#
# plot(images, titles, "gray")

####
### Adaptive
####

# src_img = cv.imread("sudoku.png")
# gray_img = cv.cvtColor(src_img, cv.COLOR_BGR2GRAY)
#
# thresh =
#
# cv.imshow("Original Image", gray_img)
# cv.imshow("Adaptive Thresholding", thresh)
#
# cv.waitKey(0)
# cv.destroyAllWindows()
