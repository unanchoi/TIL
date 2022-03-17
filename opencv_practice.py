import cv2

IMAGE = "PATH"
img = cv2.imread(IMAGE)

size = (300,300)
# option 
# 1 : rgb로 읽기(default)
# 0 : gray-scale
# -1 : rgb + alpha channel
img2 = cv2.resize(img, dsize = size, interpolation=cv2.INTER_AREA)

cv2.imshow('dog', img2) # image를 보여줌.

cv2.waitKey(5000) # == time.sleep

cv2.destroyAllWindows()

