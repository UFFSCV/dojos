import cv2
import time
import numpy as np

# Preparação do dataset
# https://drive.google.com/open?id=1MjZqA3VscsVxMpmEbc300EwZLb87NqK_
protoFile = None
weightsFile = None
nPoints = None
POSE_PAIRS = None
net = None

# Função de redimenção de imagem
resize = lambda img: cv2.resize(img, ( int(img.shape[1]/2) , int(img.shape[0]/2) ))

img = cv2.imread("input/right-frontal.jpg")
# img = cv2.imread("input/hands.jpg")
# img = cv2.imread("input/hand.jpg")

frame = None
frameCopy = None

frameWidth = None
frameHeight = None

aspect_ratio = None

threshold = None

t = time.time()
# entada das dimenções da imagem na CNN
inHeight = None
inWidth = None
print('Tamanho da entrada:',inWidth)

inpBlob = None

#Setando a Rede

output = None
print("Tempo gasto pela CNN : {:.3f}".format(time.time() - t))

points = []
print("Quantidade de pontos:",nPoints)
for i in range(nPoints):
    # Mapa de correspondencia das partes do corpo
    probMap = output[0, i, :, :]
    probMap = None

    # Encontre maxima global do probMap.

    if prob > threshold :
        # Desenhando o pontos

        # Adicione o ponto à lista se a probabilidade for maior que o limite
        points.append( )
    else :
        points.append(None)

# Desenhando o esqueleto a partir do pontos
for pair in POSE_PAIRS:
    partA = pair[0]
    partB = pair[1]
    if points[partA] and points[partB]:


# cv2.imwrite('output/Output-Keypoints.jpg', frameCopy)
# cv2.imwrite('output/Output-Skeleton.jpg', frame)

window = np.concatenate( (frameCopy,img,frame), axis=1)
cv2.imshow('Resultado',resize(window))

cv2.waitKey(0)
cv2.destroyAllWindows()
