#  pip install opencv-python

import cv2

src = cv2.imread("img.jpg",cv2.IMREAD_UNCHANGED)
# cv2.imshow("title",src)
# persentage by which img is resized
scale_parsentage=50

# calculation of 50% of dimentions
width=int(src.shape[1] * scale_parsentage/100)
hight=int(src.shape[0] * scale_parsentage/100)

# dsize
dsize=(width,hight)

# resize img
output=cv2.resize(src,dsize)

cv2.imwrite('resized_img.jpg',output)
cv2.waitKey(0)
