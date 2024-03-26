# Twitter 爬虫项目
[EnglishVersion](README_EN.md)

本项目包含两个主要脚本，用于从 Twitter 抓取推文：`set_cookies.py` 和 `spyder.ipynb`。

## set_cookies.py

- 目的：自动化登录 Twitter 并保存登录 cookies 的过程。
- 工作原理：打开 Twitter 登录页面，等待用户手动登录。30秒后，将会话 cookies 保存到文件中。

## spyder.ipynb

- 目的：使用保存的 cookies 从指定的 Twitter 搜索 URL 中抓取推文。
- 特点：加载 cookies，导航到 Twitter 搜索页面，收集推文，提取详细信息（用户名、文本、图片），并将数据保存到 JSON 文件中。

## 安装

确保已安装 Python 和 Selenium。可能需要在两个脚本中调整 ChromeDriver 的路径。

## 使用方法

1. 首先运行 `set_cookies.py` 登录并保存您的 cookies。
2. 根据需要修改 `spyder.ipynb` 中的搜索 URL。
3. 运行 `spyder.ipynb` 开始抓取推文。
