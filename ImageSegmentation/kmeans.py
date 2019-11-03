import cv2 as cv
import numpy as np

img = cv.imread("landscape.jpg")
Z = img.reshape((-1, 3))

# Ajustar o tipo do parametro
Z = np.float32(Z)

# Criterio de parada, numero de iterações e precisão
criteria =
K =
ret, label, center =

# Ajustar o tipo da resposta para o imshow
center = np.uint8(center)
res = center[label.flatten()]
res2 = res.reshape((img.shape))

cv.imshow("K-means Image",res2)
cv.waitKey(0)
cv.destroyAllWindows()
