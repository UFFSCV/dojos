import cv2 as cv
import numpy as np

img = cv.imread("landscape.jpg")
Z = img.reshape((-1, 3))

# Ajustar o tipo do parametro
Z = np.float32(Z)

# Criterio de parada, numero de iterações e precisão
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 10, 1.0)
K = 5
ret, label, center = cv.kmeans(Z, K, None, criteria, 10, cv.KMEANS_RANDOM_CENTERS)

# Ajustar o tipo da resposta para o imshow
center = np.uint8(center)
res = center[label.flatten()]
res2 = res.reshape((img.shape))

cv.imshow('res2',res2)
cv.waitKey(0)
cv.destroyAllWindows()
