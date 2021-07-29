import cv2
import numpy
import argparse
from os import replace
from pdf2image import convert_from_path

#Convert pdf to img
path = 'CN-DE-910864895-2021-3.pdf'
images = convert_from_path(path)
images[0].save(path.replace("pdf", "jpg"), 'JPEG')

#Find bar in image
img = cv2.imread(path.replace("pdf", "jpg"))
template = cv2.imread('bar.jpg')
res = cv2.matchTemplate(img, template, cv2.TM_CCORR_NORMED)
threshold = 0.7
loc = numpy.where(res >= threshold)
print(loc[1])

for pt in zip(*loc[::-1]): 
    cv2.rectangle(img, pt, (pt[0] + 5, pt[1] + 5), (0,0,255), 1)

cv2.imwrite('res.png',img)
# cut_img = img[0:171 , 0:img.shape[1]]
# cv2.imshow("Cut image", cut_img)
# cv2.waitKey(0)

