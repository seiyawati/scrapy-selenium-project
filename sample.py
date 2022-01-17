# git test
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Chromeのオプションを設定する
options = webdriver.ChromeOptions()
options.add_argument('--headless')

# Selenium Server に接続する
print('connectiong to remote browser...')
driver = webdriver.Remote(
  command_executor='http://localhost:4444/wd/hub',
  desired_capabilities=options.to_capabilities(),
  options=options,
)

# Selenium経由でブラウザを操作する
driver.get('https://www.celine.cn/CONF.343142198C.38NO')

time.sleep(10)

item_url = driver.current_url
item_name = driver.find_element(By.XPATH, '//div[@class="component-products-right__name"]')
item_price = driver.find_element(By.XPATH, '//div[@class="component-products-right__price font-neueBold mb-28"]')
print(item_name.text, item_price.text, item_url)

# ブラウザを終了する
driver.quit()
