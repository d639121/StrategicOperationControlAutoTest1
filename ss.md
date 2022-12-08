一、简介
Tesseract是一个 由HP实验室开发 由Google维护的开源的光学字符识别（OCR）引擎，可以在 Apache 2.0 许可下获得。它可以直接使用，或者（对于程序员）使用 API​​ 从图像中提取输入，包括手写的或打印的文本。

与Microsoft Office Document Imaging（MODI）相比，我们可以不断的训练的库，使图像转换文本的能力不断增强；

训练的大致流程：安装jTessBoxEditor -> 获取样本文件 -> Merge样本文件 –> 生成BOX文件 -> 定义字符配置文件 -> 字符矫正 -> 执行批处理文件 -> 将生成的 traineddata 放 入tessdata 中。

如果团队深度需要，还可以以它为模板，开发出符合自身需求的OCR引擎。

二、下载
以下是关于Tesseract的常用网址
下载地址：https://digi.bib.uni-mannheim.de/tesseract/
官方网站：https://github.com/tesseract-ocr/tesseract
官方文档：https://github.com/tesseract-ocr/tessdoc
语言包地址：https://github.com/tesseract-ocr/tessdata

注意事项:
1.尽量不要下载dev(开发中的版本)，alpha(内部测试版,一般不向外部发布,会有很多Bug)，beta(公测版本，即针对所有用户公开的测试版本)等版本。


pytesseract 库的配置：搜索找到pytesseract.py，打开该.py文件，找到 tesseract_cmd，改变它的值为刚才安装 tesseract.exe 的路径。

tesseract_cmd = "E:/Tesseract-OCR/tesseract.exe"