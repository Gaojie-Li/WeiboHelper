from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random


def init_driver():
    WINDOW_WIDTH=600
    WINDOW_HEIGHT=500
    headless = False
    incognito = True
    proxy = False
    ip, port = 0,0

    chrome_options = webdriver.ChromeOptions()
    if incognito:
        chrome_options.add_argument("--incognito")
    if headless:
        chrome_options.add_argument('--headless')
    if proxy:
        chrome_options.add_argument('--proxy-server=http://{0}:{1}'.format(ip, port))

    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.set_window_size(WINDOW_WIDTH,WINDOW_HEIGHT)

    return driver


def login(uname, upass, driver):
    login_url = "https://login.sina.com.cn/signup/signin.php?entry=sso"
    driver.get(login_url)
    time.sleep(5)

    username = driver.find_element_by_id('username')
    password = driver.find_element_by_id('password')
    smb_btn = driver.find_element_by_class_name('W_btn_a')

    # safe_login = driver.find_element_by_id('safe_login')

    print("----login in for {0}-----".format(uname))
    username.send_keys(uname)
    password.send_keys(upass)

    smb_btn.click()
    time.sleep(5)



def readOnly(tweets, freq, count):
    driver = init_driver()
    for i in range(count):
        print("="*20)
        print("READ ROUND {0}".format(i+1))
        tCount = 0
        for tweet_url in tweets:
            print("OPEN TWEET {0}".format(tCount+1))
            driver.get(tweet_url)
            print("WAIT")
            time.sleep(freq)
            tCount += 1

    driver.quit()
    print("-----close browser-----")



def read(uname, upass, tweets):
    driver = init_driver()

    driver.get('http://httpbin.org/ip')
    print(driver.page_source)

    login(uname, upass, driver)

    i = 0

    #try opening new tweets one after another
    for tweet_url in tweets:
        print("open new tweet {0}".format(i+1))
        driver.get(tweet_url)
        time.sleep(15)
        i += 1

    driver.quit()
    print("-----close browser-----")

def repost(uname, upass, tweet_url, lyrics, comment=False, upper_bound=5):
    driver = init_driver()
    login(uname, upass, driver)

    driver.get(tweet_url+"&type=repost")

    if comment:
        btn = driver.find_element_by_id("forward_comment_opt_forwardLi")
        btn.click()

    #Get relative function fields
    repost_field = driver.find_element(by=By.XPATH, value="//*[@id=\"Pl_Official_WeiboDetail__73\"]/div/div/div/div[5]/div/div[2]/div/div/div/div/div/div[1]/textarea")

    repost_btn = driver.find_element(by=By.XPATH, value="//*[@id=\"Pl_Official_WeiboDetail__73\"]/div/div/div/div[5]/div/div[2]/div/div/div/div/div/div[2]/div[1]/a")

    repost_message = repost_field.get_attribute('value')
    print(repost_message)
    lyrics_id = random.randint(0, len(lyrics)-1)
    print("SONG chosen: ", lyrics[lyrics_id])
    with open(lyrics[lyrics_id],"r") as file:
        i = 0
        for line in file:
            if i >= upper_bound:
                break
            temp =  line.strip() + repost_message
            repost_field.clear()
            time.sleep(5)
            repost_field.send_keys(temp)
            repost_btn.click()
            print("REPOST({0}) DONE".format(i+1))
            time.sleep(10 + random.randint(0,10))
            i += 1

    driver.quit()

    print("-----close browser-----")
