import cv2
import numpy as np

img_1 = cv2.imread("picture.jpg",0)
c = 1
gamma_degerler = [3.0, 4.0, 5.0]
gamma_foto = []

cv2.imshow("Original", img_1)

for gamma in gamma_degerler:
    gamma_f = c * np.power(img_1, gamma)
    gamma_foto.append(gamma_f)

for i in gamma_foto:
    cv2.imshow(i)


cv2.waitKey(0)
cv2.destroyAllWindows()