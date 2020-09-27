import numpy as np
import cv2
import functions as func

# Imagens que temos
filename1 = 'ted_cruz.jpg'
# filename1 = 'donald_trump.jpg'
# filename1 = 'hillary_clinton.jpg'
# filename1 = 'obama.jpg'

# filename2 = 'ted_cruz.jpg'
filename2 = 'donald_trump.jpg'
# filename2 = 'hillary_clinton.jpg'
# filename2 = 'obama.jpg'

# importar as imagens
print("Coletando as Imagens")
img1 =  # src
img2 =  # dst
img1Warped =

print("Coletando os pontos faciais correspondentes")
points1 =
points2 =

func.plot("Step1-FaceAlignment.jpg")

print("Criando os vetores das funções convexas")
hull1 = []
hull2 = []

print("Intersecção dos conjuntos das funções convexas, terminadas pelas distâncias euclidianas")
hullIndex =
for i in range(0, len(hullIndex)):
    hull1.append()
    hull2.append()

print("Triangularização de Delaunay aplicada pelos prontos faciais")
sizeImg2 =
rect = (0, 0, sizeImg2[1], sizeImg2[0])
dt =
if len(dt) == 0:
    quit()

print("\tAplicando a Triangularização de Delaunay")
for i in range(0, len(dt)):
    t1 = []
    t2 = []
    # Pega os pontos correspondentes dos triangulos aos das imagens
    for j in range(0, 3):
        t1.append()
        t2.append()

    # unifica a imagem com as regiões dos triangulos das imagens


func.plot("Step2-SeamlessCloning.jpg")

print("Calculando e criando a Máscara")
hull8U = []
for i in range(0, len(hull2)):
    hull8U.append()
mask =  # mask

print("Desenho dos poligonos convexos preenchidos")

print("Limitaçãos dos triangulos")
r =
center =

print("Aplicando o Seamless Cloning")
output = 

cv2.imshow("Face Swapped", output)
cv2.waitKey(0)
cv2.destroyAllWindows()
