import cv2
import numpy as np

img = cv2.imread("meteor_challenge_01.png")

if img is None:
    print("Não foi possível carregar a imagem.")
    exit()

#Convertendo a imagem para escala de cinza
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Definindo uma faixa de cor branca para a detecção de estrelas
#Corrindo problema de quando aproximava a imagem e pela perda de qualidade, não identificava a cor da mesma maneira
lower_white = np.array([200, 200, 200])
upper_white = np.array([255, 255, 255])

#Threshold para encontrar as estrelas
_, stars_binary = cv2.threshold(gray_img, 220, 255, cv2.THRESH_BINARY)

# Definindo a faixa de cor vermelha para a detecção de meteoros
lower_red = np.array([0, 0, 150])
upper_red = np.array([80, 80, 255])

#Meteoros
mask_red = cv2.inRange(img, lower_red, upper_red)

#Estrelas
mask_white = cv2.inRange(img, lower_white, upper_white)

stars_count = cv2.countNonZero(mask_white)
meteors_count = cv2.countNonZero(mask_red)

print("Número de Estrelas:", stars_count)
print("Número de Meteoros:", meteors_count)
