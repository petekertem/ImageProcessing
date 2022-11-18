import numpy as np
import cv2
import matplotlib.pyplot as plt

foto = cv2.imread("images.jfif",0) # 0 fotoğrafı siyah-beyaz yükler

def fotograf_negatifi(foto):
    L = np.max(foto) #255
    negatif_foto = L - foto
    return negatif_foto

negatif_foto = fotograf_negatifi(foto)
plt.imshow(negatif_foto, cmap="gray")
plt.show()