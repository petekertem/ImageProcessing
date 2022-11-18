import cv2
import numpy as np

img = cv2.imread("picture.jpg", 0)
print(img.dtype)

c = 5

logarithm = c * (np.log(img + 1))
logarithm = np.array(logarithm, dtype=np.uint8)

cv2.imshow("Original", img)
cv2.imshow("logarithm", logarithm)
cv2.waitKey(0)
cv2.destroyAllWindows()
