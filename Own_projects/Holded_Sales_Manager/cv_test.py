from os import replace
from pdf2image import convert_from_path
import cv2

path = 'CN-DE-910864895-2021-3.pdf'
images = convert_from_path(path)
images[0].save(path.replace("pdf", "jpg"), 'JPEG')

img = cv2.imread(path.replace("pdf", "jpg"))
cut_img = img[700:1020, 96:700]
cv2.imshow("Cut image", cut_img)
cv2.waitKey(0)

