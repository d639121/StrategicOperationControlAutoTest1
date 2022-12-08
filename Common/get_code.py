import cv2 as cv
from selenium.webdriver.common.by import By
from Common.tools.ocr import ocr


def get_code(driver):
    # 点击验证码，切换图片
    driver.implicitly_wait(2)
    driver.find_element(By.ID, "canvasCode").click()
    # 找到图片的位置
    canvas = driver.find_element(By.ID, "canvasCode")
    # 发现屏幕上canvas绘制的图表
    canvas.location_once_scrolled_into_view
    # 将canvas绘制的图表生成图片
    canvas.screenshot(r"../Common/image/yzm.png")
    # 对图片进行预处理
    src = cv.imread(r"../Common/image/yzm.png")
    # 调用识别验证码方法，并返回识别到的图像
    code = ocr(src)
    # 去除所有的空格
    code = "".join(code.split())
    return code