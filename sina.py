from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random


def init_driver():
    # WINDOW_WIDTH=1000
    # WINDOW_HEIGHT=800
    headless = False
    incognito = True
    proxy = False
    ip, port = "144.202.53.250","8080"

    chrome_options = webdriver.ChromeOptions()
    if incognito:
        chrome_options.add_argument("--incognito")
    if headless:
        chrome_options.add_argument('--headless')
    if proxy:
        chrome_options.add_argument('--proxy-server=http://{0}:{1}'.format(ip, port))

    driver = webdriver.Chrome(chrome_options=chrome_options)
    # driver.set_window_size(WINDOW_WIDTH,WINDOW_HEIGHT)

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

#Select a random song and repost with lyrics
def repostLyrics(driver, tweet_url, lyrics, comment=False, upper_bound=5):
    # driver = init_driver()
    # login(uname, upass, driver)

    openPage(driver, tweet_url)

    lyrics_id = random.randint(0, len(lyrics)-1)
    print("SONG chosen: ", lyrics[lyrics_id])
    with open(lyrics[lyrics_id],"r") as file:
        i = 0
        for line in file:

            if i >= upper_bound:
                break
            #Get relative function fields

            if comment:
                btn = driver.find_element_by_id("forward_comment_opt_forwardLi")
                btn.click()

            try:
                print("Attempting Repost({0})".format(i+1))
                repost_field, repost_btn, repost_message = getRepostFields(driver)

                temp =  line.strip() + repost_message
                if post(driver, repost_field, repost_btn, temp):
                    print("Repost({0}) Done".format(i+1))
                    i += 1
            except Exception as e:
                print("Error: ", str(e))

    driver.quit()

    print("-----close browser-----")

#Repost with given repost messages
def repost(driver, tweet_url, reposts, comment=False, upper_bound=5):
    # driver = init_driver()
    # driver.get('http://httpbin.org/ip')
    # print(driver.page_source)

    # login(uname, upass, driver)

    openPage(driver, tweet_url)
    selected = set()
    repostCount = 0
    while repostCount < min(upper_bound, len(reposts)):
        try:
            print("Attempting Repost({0})".format(repostCount+1))
            if comment:
                btn = driver.find_element_by_id("forward_comment_opt_forwardLi")
                btn.click()

            repost_field, repost_btn, repost_message = getRepostFields(driver)

            #randomly select a repost message
            i = random.randint(0, len(reposts)-1)

            while i in selected:
                if len(selected) == len(reposts):
                    return
                i = random.randint(0, len(reposts)-1)
            selected.add(i)

            temp =  reposts[i] + repost_message
            if post(driver, repost_field, repost_btn, temp):
                print("Repost({0}) Done".format(repostCount+1))
                repostCount += 1

        except Exception as e:
            print("\tERROR: ", str(e))

    driver.quit()

    print("-----close browser-----")

def openPage(driver, tweet_url):
    if "?" in tweet_url:
        tweet_url = tweet_url + "&type=repost"
    else:
        tweet_url = tweet_url + "?" + "&type=repost"
    print("Tweet url: {0}".format(tweet_url))
    driver.get(tweet_url)

def getRepostFields(driver):
    repost_field = driver.find_element(by=By.XPATH, value="//*[@id=\"Pl_Official_WeiboDetail__73\"]/div/div/div/div[5]/div/div[2]/div/div/div/div/div/div[1]/textarea")

    repost_btn = driver.find_element(by=By.XPATH, value="//*[@id=\"Pl_Official_WeiboDetail__73\"]/div/div/div/div[5]/div/div[2]/div/div/div/div/div/div[2]/div[1]/a")

    repost_message = repost_field.get_attribute('value')
    # print(repost_message)
    return repost_field, repost_btn, repost_message

def post(driver, repost_field, repost_btn, repost_message):
    if len(repost_message) > 140:
        handleRepostTooLong(repost_message)
        driver.refresh()
        return False
    print("\tRepost Message:\n\t{0}".format(repost_message))
    repost_field.clear()
    time.sleep(5 + random.randint(0,2))
    repost_field.send_keys(repost_message)
    repost_btn.click()

    driver.refresh()
    time.sleep(10 + random.randint(0,10))
    return True


def handleRepostTooLong(message):
    print("\tERROR: Repost Message too long")
    print("\t"+message + "\n")
