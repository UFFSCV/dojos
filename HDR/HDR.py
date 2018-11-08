import cv2
import numpy as np
import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt

#Pegar os tempos de abertura de câmera
times = []

filenames = []
images = []
hdr = []

#Importando as Imagens
for filename in filenames:
    img = None
    images.append(img)

fig=plt.figure(figsize=(10, 10))
fig.canvas.set_window_title("Imagens Capturadas")
columns,rows = 2, 2
times_labels = [ "0.033", "0.25", "2.5", "15.0" ]
for i in range(1, columns*rows +1):
    img = images[i-1]
    fig.add_subplot(rows, columns, i)
    plt.axis('off')
    plt.title("Exposição de {} segundos".format(times_labels[i-1]))

    plt.imshow( )

plt.show()

print("Alinhando a mediada do limite de bitmaps")

print("Calibrando CRF")

print("Unindo as  Imagens")

# Metodos de HDR
# Drago
print("Gerando HDR Draco")

# Durand
print("Gerando HDR Durand")

# Reinhard
print("Gerando HDR Reinhard")

# Mantiuk
print("Gerando HDR Mantiuk")

# Resultados Finais
print("Gerando resultados Finais")
fig=plt.figure(figsize=(10, 10))
fig.canvas.set_window_title("Resultado da aplicação de HDR")
columns,rows = 2, 2
hdr_method = ["Draco","Durand","Reinhard","Matiuk"]
for i in range(1, columns*rows +1):
    img = hdr[i-1]
    fig.add_subplot(rows, columns, i)
    plt.axis('off')
    plt.title(hdr_method[i-1])

    plt.imshow( )
    
plt.show()
