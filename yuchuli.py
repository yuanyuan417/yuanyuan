import cv2 as cv
src=cv.imread('F:\pig-picture\IMG_20190810_162630_BURST3.jpg')#括号内是图片在路径，不可出现中文字符
cv.namedWindow('input_image', cv.WINDOW_AUTOSIZE)#以input-image命名加载出的图片
cv.imshow('input_image', src)
cv.waitKey(0)
cv.destroyAllWindows()