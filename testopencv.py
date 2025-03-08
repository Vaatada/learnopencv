
import cv2

img=cv2.imread('C:\\Users\Lenovo\Desktop\image\img2.jpg')

new_width=800
new_height=600
img1=cv2.resize(img,(new_width,new_height))

cv2.imshow('img',img)
cv2.imshow('img1',img1)

cv2.waitKey(0)
