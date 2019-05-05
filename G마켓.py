from selenium import webdriver

chrome_path = "C:/Users/jhunyeom/Desktop/coding/webdrivers/chromedriver.exe"
driver = webdriver.Chrome(chrome_path)

url = "http://corners.gmarket.co.kr/Bestsellers/"
driver.get(url)

title_list = driver.find_elements_by_class_name('itemname')
clean_titles = []

for i in title_list:
    if len(i.text.encode('utf-8')) != 0:
        clean_titles.append(i.text)

cut_titles = clean_titles[:10]

for i in cut_titles:
    print i

driver.quit()
