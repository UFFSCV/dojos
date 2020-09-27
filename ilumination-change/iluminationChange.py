import cv2
import numpy as np
import math
import matplotlib.pyplot as plt

img = cv2.imread("input/flor.jpg")
resize = lambda img: cv2.resize(img, ( int(img.shape[1]/2) , int(img.shape[0]/2) ))

# GAMMA
# https://en.wikipedia.org/wiki/Gamma_correction
# Gamma values < 1 will shift the image towards the darker end of the spectrum while
# Gamma values > 1 will make the image appear lighter. A gamma value of G=1 will have no affect on the input image:
# https://en.wikipedia.org/wiki/Gamma_correction
def gamma_ajust(img,gamma):


gammas = [0, 0.5, 1, 1.5, 2, 2.5]
gammas_img = []
for gamma in gammas:
    gammas_img.append(gamma_ajust(img,gamma))
    print(f" Gamma = {gamma}")
print()
row1 = np.concatenate((gammas_img[0],gammas_img[1],gammas_img[2]),axis=1)
row2 = np.concatenate((gammas_img[3],gammas_img[4],gammas_img[5]),axis=1)
window = np.concatenate((row1,row2), axis=0)
cv2.imshow("Gamma" ,resize(window))
cv2.imshow("Imagem Original",img)

cv2.waitKey(0)
cv2.destroyAllWindows()


# BRILHO E CONTRASTE
# https://en.wikipedia.org/wiki/Brightness
# https://en.wikipedia.org/wiki/Contrast_(vision)
# https://docs.opencv.org/3.4/d3/dc1/tutorial_basic_linear_transform.html
def brightness_contrast_adjustment(img,beta,alpha):


alphas = [0.1,0.5,1,1.5,2,2.5]
betas = [1,10,20,30,40,50]
for alpha in alphas:
    imgs = []
    for beta in betas:
        imgs.append()
        print(f" Alpha={alpha} \tBeta={beta}")

    row1 = np.concatenate((imgs[0],imgs[1],imgs[2]),axis=1)
    row2 = np.concatenate((imgs[3],imgs[4],imgs[5]),axis=1)
    window = np.concatenate((row1,row2), axis=0)

    cv2.imshow('Resultados Alpha {}'.format(alpha,beta), window)
    print()
cv2.imshow("Imagem Original",img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# BALANCEAMENTO DE COR
# https://en.wikipedia.org/wiki/Color_balance
# https://web.stanford.edu/~sujason/ColorBalancing/simplestcb.html
# http://www.morethantechnical.com/2015/01/14/simplest-color-balance-with-opencv-wcode/
def apply_mask():

def apply_threshold():

def simpleCB( ):

window = np.concatenate((img,simpleCB( )), axis=1)
cv2.imshow('Imagem Original VS. Imagem Cor Balanceada ', window)

cv2.waitKey(0)
cv2.destroyAllWindows()
