import cv2
import numpy as np

img_black = np.zeros((28, 28, 3), dtype=np.uint8)

blue_color = (255, 0, 0)  
img_blue = np.full((256, 256, 3), blue_color, dtype=np.uint8)

cv2.imwrite("img_black.png", img_black)
cv2.imwrite("img_blue.png", img_blue)

print("Imagens salvas: img_black.png (28x28 preta) e img_blue.png (256x256 azul)")
