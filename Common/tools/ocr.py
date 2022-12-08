import cv2 as cv
import pytesseract
from PIL import Image



def ocr(image):
    # 边缘保留滤波  去噪
    blur = cv.pyrMeanShiftFiltering(image, sp=8, sr=60)
    # 灰度图像
    gray = cv.cvtColor(blur, cv.COLOR_BGR2GRAY)
    # 二值化
    ret, binary = cv.threshold(gray, 160, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
    # 形态学操作  获取结构元素  开操作
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 2))
    bin1 = cv.morphologyEx(binary, cv.MORPH_OPEN, kernel)
    kernel = cv.getStructuringElement(cv.MORPH_OPEN, (2, 3))
    bin2 = cv.morphologyEx(bin1, cv.MORPH_OPEN, kernel)
    # 逻辑运算  让背景为白色  字体为黑  便于识别
    cv.bitwise_not(bin2, bin2)
    # 识别
    test_message = Image.fromarray(bin2)
    text = pytesseract.image_to_string(test_message)
    # 去除结果
    text = "".join(text.split())
    print('识别结果:', text)
    return text

# src = cv.imread(r'../image/yzm.png')
# cv.imshow('input image', src)
# ocr(src)
# cv.waitKey(0)
# cv.destroyAllWindows()
