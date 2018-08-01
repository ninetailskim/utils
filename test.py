from skimage.measure import compare_ssim as ssim
from skimage.measure import compare_psnr as psnr
import cv2
'''
x = cv2.imread('GT/IMG_0003/GT/00005.jpg')

y = cv2.imread('GT/IMG_0003/input/00005.jpg')

z = cv2.imread('DVDresult/IMG_0003/00005.jpg')

q = cv2.imread('0619sepe1d284000/IMG_0003/00005.png')

print(x.shape, y.shape, z.shape, q.shape)
print(psnr(x, y))
print(psnr(x, z))
cv2.imshow('gt',x)
cv2.imshow('input',y)
cv2.imshow('out',z)
cv2.waitKey(0)
cv2.destroyAllWindows()

H = 704
W = 1280

x = x[:H, :W, :]
y = y[:H, :W, :]
z = z[:H, :W, :]

print(x.shape, y.shape, z.shape, q.shape)
print("x~y",psnr(x, y))
print("y~x",psnr(y, x))
print("x~z",psnr(x, z))
print("x~q",psnr(x, q))
cv2.imshow('gt',x)
cv2.imshow('input',y)
cv2.imshow('out',z)
cv2.imshow('myout',q)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(3 //2)

print('model-123' > 'model-1230')

real = []

for i in range(5):
    real.append([i,i*2])

for i in range(5):
    print(real[i][0],real[i][1])
'''
x = [1] * 3

for i in range(3):
    print(x[i])


y = [[1 * i] * 3 for i in range(5)]
print(y[4][1])
for i in range(3):
    print(y[:][i])

for i in range(0):
    print("1q2w3eq")