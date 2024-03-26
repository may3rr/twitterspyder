import json
import time
import os
from selenium import webdriver

browser = webdriver.Chrome()

try:
    browser.get("https://twitter.com/i/flow/login")
    time.sleep(30)  # 30s内登录等待退出

finally:
    dictCookies = browser.get_cookies()
    jsonCookies = json.dumps(dictCookies)
    
    # 检查文件夹是否存在，不存在则创建
    if not os.path.exists('twitter_Crawler'):
        os.makedirs('twitter_Crawler')
    
    # 保存cookies到文件
    with open('twitter_Crawler/twitter_cookie.json', 'w') as f:
        f.write(jsonCookies)
    browser.quit()
