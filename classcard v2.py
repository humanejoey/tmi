from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


class AutomateClassCard:
    def __init__(self, username, password, week_url):
        self.driver = self.driver_setup()
        self.delay = 5
        self.week_url = week_url

        self.xpath = {
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

        self.login(username, password)

    @staticmethod
    def driver_setup():
        chrome_path = "C:/Users/jhunyeom/Desktop/coding/webdrivers/chromedriver.exe"
        driver = webdriver.Chrome(chrome_path)
        return driver

    def login(self, username, password):
        self.driver.get('http://www.classcard.net/Login')
        username_input = WebDriverWait(self.driver, self.delay).until(
            EC.presence_of_element_located((By.XPATH, self.xpath["username_input"])))
        username_input.send_keys(username)
        password_input = self.driver.find_element_by_xpath(self.xpath["password_input"])
        password_input.send_keys(password)
        login_btn = self.driver.find_element_by_xpath(self.xpath["login_btn"])
        login_btn.click()
        WebDriverWait(self.driver, self.delay).until(EC.presence_of_element_located((By.XPATH, self.xpath["class_name"])))

    def get_week_page(self):
        self.driver.get(self.week_url)
        dropdown = WebDriverWait(self.driver, self.delay).until(EC.presence_of_element_located((By.XPATH, self.xpath["dropdown"])))
        dropdown.click()
        all_card = WebDriverWait(self.driver, self.delay).until(EC.presence_of_element_located((By.XPATH, self.xpath["all_cards"])))
        all_card.click()

    def memorize(self):
        self.get_week_page()
        memorize_btn = WebDriverWait(self.driver, self.delay).until(EC.presence_of_element_located((By.XPATH, self.xpath["memorize"])))
        memorize_btn.click()
        time.sleep(self.delay)
        word_cnt = int(self.driver.find_elements_by_class_name('unknown_count')[0].text)
        WebDriverWait(self.driver, self.delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'btn-cover-down')))

        for i in range(word_cnt):
            time.sleep(self.delay)
            actions = ActionChains(self.driver)
            actions.send_keys(Keys.SPACE)
            actions.perform()
            actions.send_keys(Keys.ENTER)
            actions.perform()

    def recall(self):
        self.get_week_page()
        recall_btn = WebDriverWait(self.driver, self.delay).until(EC.presence_of_element_located((By.XPATH, self.xpath["recall"])))
        recall_btn.click()
        time.sleep(self.delay)
        word_cnt = int(self.driver.find_elements_by_class_name('unknown_count')[0].text)

        for i in range(word_cnt):
            time.sleep(self.delay)
            answer_element = WebDriverWait(self.driver, self.delay).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'answer')))
            answer_element.click()
            self.driver.refresh()

    def spell(self):
        self.get_week_page()
        spell_btn = WebDriverWait(self.driver, self.delay).until(EC.presence_of_element_located((By.XPATH, self.xpath["spell"])))
        spell_btn.click()

        time.sleep(2)
        word_cnt = int(self.driver.find_elements_by_class_name('unknown_count')[0].text)

        for i in range(word_cnt):
            time.sleep(self.delay)
            setting_btn = WebDriverWait(self.driver, self.delay).until(
                EC.presence_of_element_located((By.XPATH, self.xpath["setting"])))
            setting_btn.click()
            radio_btn1 = WebDriverWait(self.driver, self.delay).until(EC.presence_of_element_located((By.XPATH, self.xpath["radio1"])))
            radio_btn1.click()
            time.sleep(1)
            answer_span = WebDriverWait(self.driver, self.delay).until(
                EC.presence_of_element_located((By.XPATH, self.xpath["answer_span"])))
            answer = str(answer_span.text)
            radio_btn2 = WebDriverWait(self.driver, self.delay).until(EC.presence_of_element_located((By.XPATH, self.xpath["radio2"])))
            radio_btn2.click()
            time.sleep(1)
            answer_input = WebDriverWait(self.driver, self.delay).until(
                EC.presence_of_element_located((By.XPATH, self.xpath["answer_input"])))
            answer_input.send_keys(answer)
            actions = ActionChains(self.driver)
            actions.send_keys(Keys.ENTER)
            actions.perform()
            self.driver.refresh()
