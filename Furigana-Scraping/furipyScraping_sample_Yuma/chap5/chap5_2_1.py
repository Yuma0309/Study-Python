import time
from selenium import webdriver
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
options.add_argument('--headless')  # ヘッドレスモードでChromeを実行（オプション）

driver = webdriver.Chrome(options=options)
driver.get('https://www.watch.impress.co.jp/')
time.sleep(5)
soup = BeautifulSoup(driver.page_source, 'html.parser')
articles = soup.select('#allsite-access-ranking-ul-latest > li')
for article in articles:
    print(article.text)
