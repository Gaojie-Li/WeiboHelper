import pickle
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import sina

def saveCookies(uname, upass, ip, port, proxy):
    print("Save Cookies for {0}".format(uname))
    if os.path.exists("Cookies/{0}.pkl".format(uname)):
        print("Cookies for {0} already exists".format(uname))
        return
    driver = sina.init_driver(ip, port, proxy)
    driver.get("http://weibo.com")

    username = driver.find_element(by=By.ID, value="loginname")
    password = driver.find_element(By.NAME, value="password")
    smb_btn = driver.find_element(By.XPATH, value="//*[@id=\"pl_login_form\"]/div/div[3]/div[6]/a")

    username.send_keys(uname)
    password.send_keys(upass)
    smb_btn.click()

    time.sleep(50)
    pickle.dump(driver.get_cookies(), open("Cookies/{0}.pkl".format(uname),"wb"))
    # print(driver.get_cookies())
    print("Done Saving Cookies for {0}".format(uname))
    driver.quit()


def loadCookies(uname, ip, port, proxy=False):
    print("Load Cookies for {0}".format(uname))

    driver = sina.init_driver(ip, port, proxy)
    driver.get("https://www.weibo.com/")
    time.sleep(5)
    cookies = pickle.load(open("Cookies/{0}.pkl".format(uname), "rb"))
    # print(cookies)
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.refresh()
    time.sleep(5)
    return driver
