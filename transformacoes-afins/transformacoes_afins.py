import cv2
import numpy as np

def identidade(image):
    return  pass

def reflexao(image,axis):
    return  pass

def rotacao(image, angulo, centro=None, escala=1.0):
    return  pass

def traslacao(image,x,y):
    return  pass

def cisalhamento(image):
    return  pass
def cisalhamento_triangular(image):
    return  pass

img = cv2.imread('imgs/paisagem.jpg')

# IMAGEM ORIGINAL
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# IMAGEM IDENTIDADE
img_identidade = identidade(img)
cv2.imshow('img_identidade',img_identidade)
cv2.waitKey(0)
cv2.destroyAllWindows()

# IMAGEM REFLETIDA
img_refletida = reflexao(img)
cv2.imshow('img_refletida',img_refletida)
cv2.waitKey(0)
cv2.destroyAllWindows()

# IMAGEM ROTACIONADA
img_rotacionada = rotacao(img,60)
cv2.imshow('img_rotacionada',img_rotacionada)
cv2.waitKey(0)
cv2.destroyAllWindows()

# IMAGEM TRANSLADADA
img_transalada = traslacao(img,200,100)
cv2.imshow('img_transalada',img_transalada)
cv2.waitKey(0)
cv2.destroyAllWindows()

# IMAGEM CISALHADA
img_cisalhada = cisalhamento(img)
cv2.imshow('img_cisalhada',img_cisalhada)
cv2.waitKey(0)
cv2.destroyAllWindows()

# DESENHO DDO TRIANGULO


# IMAGEM CISALHADA TRIANGULAR
cv2.imshow('img',img)
cisalhamento_triangular = cisalhamento_triangular(img)
cv2.imshow('cisalhamento_triangular',cisalhamento_triangular)
cv2.waitKey(0)
cv2.destroyAllWindows()


""" DESAFIO
    Pegar a imagem grid.jpg, desenhar três pontos nela e aplicar 
    o cisalhamento para:
    - O ponto A aumentar 10px em X e Y
    - O ponto A aumentar 10px em X e o B 10px em Y
    - O ponto C aumentar 20px em X 30 px em Y
    Salvar as 3 imagens e comparar os comportamentos para cada uma
    delas.
"""