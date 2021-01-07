import cv2

img = cv2.imread("/media/bv/d/UpperAI/Indoor/zz/卫生间/zz_0.jpg")
shape = img.shape
print(shape)

cv2.imshow("test", img)
cv2.waitKey(0)

img2 = cv2.resize(img, (int(shape[1]/2), int(shape[0]/2)))
shape = img2.shape
print(shape)

cv2.imshow("test", img2)
cv2.waitKey(0)
