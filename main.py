import cv2
import numpy as np

#Carregando imagem
img = cv2.imread("meteor_challenge_01.png")

if img is None:
    print("Não foi possível carregar a imagem.")
    exit()

#Adicionando a cor das estrelas
mask_white = cv2.inRange(img, (255, 255, 255), (255, 255, 255))

#Adicionando a cor dos meteoros
mask_red = cv2.inRange(img, (0, 0, 255), (0, 0, 255))

#Contando os pixels de cada cor
stars_count = cv2.countNonZero(mask_white)
meteors_count = cv2.countNonZero(mask_red)

print("Número de Estrelas:", stars_count)
print("Número de Meteoros:", meteors_count)

#Adicionando a cor da água
mask_blue = cv2.inRange(img, (255, 0, 0), (255, 0, 0))

meteors_in_water = 0

#Percorre todas as colunas da imagem
#Caso seja verificado que há pixels azuis e pixels vermelhos na respectiva coluna, deve-se contabilizar a quant de pixels vermelhos da coluna
for x in range(img.shape[1]):  
    blue_found = False 
    red_found = False  
    
    #Verifica se há um pixel azul na coluna
    if np.any(mask_blue[:, x] != 0):
        blue_found = True

    #Verifica se há um pixel vermelho na coluna
    if np.any(mask_red[:, x] != 0):
        red_found = True

    #Caso ambas as condições sejam verdadeiras, adicionamos os meteoros à contagem
    if blue_found and red_found:
        meteors_per_column = cv2.countNonZero(mask_red[:, x])  
        #Adicionando o número de meteoros da coluna na água
        meteors_in_water += meteors_per_column  

print("Meteoros caindo na água:", meteors_in_water)
