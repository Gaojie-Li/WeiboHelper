import pickle
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
import os
import sina

def saveCookies(uname, upass, ip="", port="", headless=False,proxy=False, force=False):
    print("Save Cookies for {0}".format(uname))

    if os.path.exists("Cookies/{0}.pkl".format(uname)) and not force:
        print("Cookies for {0} already exists".format(uname))
        return False, None
    driver = sina.init_driver(ip, port, proxy,headless=headless)

    driver.get("http://weibo.com")
    time.sleep(10)

    username = driver.find_element(by=By.ID, value="loginname")
    password = driver.find_element(By.NAME, value="password")
    # smb_btn=WebDriverWait(driver,10).until(lambda x:x.find_element(By.XPATH, value="//*[@id=\"pl_login_form\"]/div/div[3]/div[6]/a"))
    smb_btn = driver.find_element(By.XPATH, value="//*[@id=\"pl_login_form\"]/div/div[3]/div[6]/a")

    username.clear()
    password.clear()
    username.send_keys(uname)
    password.send_keys(upass)
    smb_btn.click()

    time.sleep(5)

    #TODO: investigate verify code issue, return True even if no verify code is required

    # if isVerifyCodeExist(driver):
    #     inputVerifyCode(driver)

    # sina.inputVerifyCode(driver)

    time.sleep(50)
    pickle.dump(driver.get_cookies(), open("Cookies/{0}.pkl".format(uname),"wb"))
    print(driver.get_cookies())
    print("Done Saving Cookies for {0}".format(uname))

    # driver.quit()
    return True, driver



def loadCookies(uname, ip="", port="", proxy=False,headless=False):
    print("Load Cookies for {0}".format(uname))

    driver = sina.init_driver(ip, port, proxy,headless=headless)
    driver.get("https://www.weibo.com/")
    time.sleep(5)
    cookies = pickle.load(open("Cookies/{0}.pkl".format(uname), "rb"))
    # print(cookies)
    for cookie in cookies:
        driver.add_cookie(cookie)

    driver.refresh()
    time.sleep(5)

    #update cookie
    pickle.dump(driver.get_cookies(), open("Cookies/{0}.pkl".format(uname),"wb"))
    return driver


# 根据验证框的存在与否判断是否要输入验证码
def isVerifyCodeExist(driver):
    try:# 如果成功找到验证码输入框返回true
        driver.find_element_by_css_selector('input[name="verifycode"]')
        print("Found verify code")
        return True
    except:# 如果异常返回false
        print("No verify code found")
        return False


# 输入验证码部分，如果无需输入则直接返回，否则手动输入成功后返回
def inputVerifyCode(driver):
    input_verifycode=driver.find_element_by_css_selector('input[name="verifycode"]')# 验证码输入框
    bt_change=driver.find_element_by_css_selector('img[action-type="btn_change_verifycode"]')# 验证码图片，点击切换
    bt_logoin=driver.find_element_by_class_name('login_btn')# 登录按钮
    while isVerifyCodeExist(driver):# 如果验证码输入框一直存在，则一直循环
        print(u'请输入验证码……(输入"c"切换验证码图片)')
        verifycode=input()
        if verifycode=='c':
            bt_change.click()
        else:
            input_verifycode.send_keys(verifycode)
            bt_logoin.click()
            # 点击完登录以后判断是否成功
            if driver.current_url.split('/')[-1]=='home':# 如果连接已经跳转到home
                print(u'登录成功')
                break
            else:
                print(u'输入的验证码不正确')
