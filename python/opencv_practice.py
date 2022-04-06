import cv2

IMAGE = "PATH"
img = cv2.imread(IMAGE)
size = (300,300)
# option 
# 1 : BGR로 읽기(default)
# 0 : gray-scale
# -1 : BGR + alpha channel

img_toHSV = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # 이미지 컬러 공간 변환 to HSV

#Image를 resize
# 보간법(Interpolation)을 설정해줘야 함.
img2 = cv2.resize(img, dsize = size, interpolation=cv2.INTER_AREA)


cv2.imshow('dog', img2) # image를 보여줌.

cv2.waitKey(5000) # == time.sleep

cv2.destroyAllWindows() # img show 창 닫기


# Image Crop
img3 = img[100:500, 200:400]
# [y start: y end , x start : x end]


# Image Blur
img4 = cv2.blur(img, (2,2), anchor=(-1,-1), borderType=cv2.BORDER_DEFAULT)
img5 = cv2.blur(img, (2,2), anchor=(-1,-1), borderType=cv2.BORDER_ISOLATED)


#Image Save
cv2.imwrite('dog_after.jpg', img5)


#cv2.split() => 이미지 채널 분리
#cv2.merge() => 이미지 채널 합치기

import numpy as np
x = [1,2,3,4,5,6,7,8,9,10]
A = np.float64(np.array(x))
B = np.float64(np.zeros(10))

# 이미지를 normalize
cv2.normalize(A,B,0,1, cv2.NORM_MINMAX) 
