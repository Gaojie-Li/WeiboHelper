from selenium import webdriver
from selenium.webdriver.common.by import By
from collections import defaultdict
import time


def test_weibo():
    readable = open("./config.txt")

    user_pass = defaultdict(str)
    for line in readable:
        parts = line.split('----')
        # user_pass[parts[0]] = parts[1]
        username = parts[0]
        password = parts[1]

    chrome_option = webdriver.ChromeOptions()
    chrome_option.add_argument("--incognito")
    driver = webdriver.Chrome('./chromedriver', chrome_options=chrome_option)
    driver.set_window_size(1500, 800)

    driver.get("http://weibo.com")
    time.sleep(3)

    login_field = driver.find_element(by=By.ID, value="loginname")
    password_field = driver.find_element(By.NAME, value="password")
    submit_button = driver.find_element(
        By.XPATH, value="//*[@id=\"pl_login_form\"]/div/div[3]/div[6]/a")

    # for key, value in user_pass.items():
    # login_field.send_keys(key)
    # password_field.send_keys(value)
    # submit_button.click()
    # time.sleep(20)
    login_field.send_keys(username)
    password_field.send_keys(password)
    submit_button.click()
    time.sleep(15)

    search_field = driver.find_element(
        by=By.XPATH, value="//*[@id=\"plc_top\"]/div/div/div[2]/input")
    search_field.send_keys("尤长靖")
    search_button = driver.find_element(
        by=By.XPATH, value="//*[@id=\"plc_top\"]/div/div/div[2]/a")
    search_button.click()
    time.sleep(5)

    name_button = driver.find_element(
        by=By.XPATH, value="//*[@id=\"pl_weibo_directtop\"]/div/div/div/div[2]/p[1]/a[1]")
    name_button.click()
    time.sleep(15)


test_weibo()
