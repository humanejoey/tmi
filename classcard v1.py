from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

chrome_path = "C:/Users/jhunyeom/Desktop/coding/webdrivers/chromedriver.exe"
driver = webdriver.Chrome(chrome_path)
delay = 5

xpath = {
    "username_input": '//*[@id="login_id"]',
    "password_input": '//*[@id="login_pwd"]',
    "login_btn": '//*[@id="loginForm"]/div[2]/button',
    "class_name": '/html/body/div[1]/div[2]/div/div/div[1]/div[3]/div[2]/a',
    "week_name": '/html/body/div[1]/div[2]/div/div/div[2]/div[3]/div/div[1]/div[2]/div[1]/a',
    "dropdown": '/html/body/div[1]/div[5]/div[2]/div[1]/div[2]/a',
    "all_cards": '/html/body/div[1]/div[5]/div[2]/div[1]/div[2]/ul/li[1]/a',
    "memorize": '//*[@id="tab_set_all"]/div[1]/div/div[2]/a[1]',
    "recall": '//*[@id="tab_set_all"]/div[1]/div/div[2]/a[2]',
    "spell": '//*[@id="tab_set_all"]/div[1]/div/div[2]/a[3]',
    "answer_input": '//*[@id="wrapper-learn"]/div/div/div[2]/div[2]/div[1]/div[2]/div/div[2]/input',
    "setting": '/html/body/div[1]/div/div[2]/div[3]/a',
    "radio1": '//*[@id="show_type_1"]',
    "radio2": '//*[@id="show_type_0"]',
    "answer_span": '//*[@id="wrapper-learn"]/div/div/div[2]/div[2]/div[1]/div[1]/div/div[1]/span[1]',
}

url = 'http://www.classcard.net/Login'
driver.get(url)

username = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, xpath["username_input"])))
username.send_keys("")
password = driver.find_element_by_xpath(xpath["password_input"])
password.send_keys("")
login_btn = driver.find_element_by_xpath(xpath["login_btn"])
login_btn.click()

class_link = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, xpath["class_name"])))
class_link.click()

week_link = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, xpath["week_name"])))
week_link.click()


def memorize_sequence():
    dropdown = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, xpath["dropdown"])))
    dropdown.click()

    all_card = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, xpath["all_cards"])))
    all_card.click()

    memorize_btn = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, xpath["memorize"])))
    memorize_btn.click()

    time.sleep(2)
    word_cnt = int(driver.find_elements_by_class_name('unknown_count')[0].text)
    focus_element = WebDriverWait(driver, delay).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'btn-cover-down')))

    for i in range(word_cnt):
        time.sleep(3)
        actions = ActionChains(driver)
        actions.send_keys(Keys.SPACE)
        actions.perform()
        actions.send_keys(Keys.ENTER)
        actions.perform()


def recall_sequence():
    dropdown = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, xpath["dropdown"])))
    dropdown.click()
    all_card = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, xpath["all_cards"])))
    all_card.click()

    recall_btn = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, xpath["recall"])))
    recall_btn.click()

    time.sleep(2)
    word_cnt = int(driver.find_elements_by_class_name('unknown_count')[0].text)

    for i in range(word_cnt):
        time.sleep(5)
        answer_element = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'answer')))
        answer_element.click()
        driver.refresh()


def spell_sequence():
    dropdown = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, xpath["dropdown"])))
    dropdown.click()
    all_card = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, xpath["all_cards"])))
    all_card.click()

    spell_btn = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, xpath["spell"])))
    spell_btn.click()

    time.sleep(2)
    word_cnt = int(driver.find_elements_by_class_name('unknown_count')[0].text)

    for i in range(word_cnt):
        time.sleep(3)
        setting_btn = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, xpath["setting"])))
        setting_btn.click()
        radio_btn1 = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, xpath["radio1"])))
        radio_btn1.click()
        time.sleep(1)
        answer_span = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, xpath["answer_span"])))
        answer = str(answer_span.text)
        radio_btn2 = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, xpath["radio2"])))
        radio_btn2.click()
        time.sleep(1)
        answer_input = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, xpath["answer_input"])))
        answer_input.send_keys(answer)
        actions = ActionChains(driver)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        driver.refresh()


spell_sequence()

# driver.quit()
