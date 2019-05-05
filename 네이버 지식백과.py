from selenium import webdriver

chrome_path = "C:/Users/jhunyeom/Desktop/coding/webdrivers/chromedriver.exe"

driver = webdriver.Chrome(chrome_path)

url = "https://terms.naver.com/"
driver.get(url)

title_raw = driver.find_elements_by_class_name("title")
title_clean = []

for t in title_raw:
    if len(t.text.encode('utf-8')) != 0 and t.tag_name == 'strong':
        title_clean.append(t.text)

for t in title_clean:
    print t

driver.quit()
