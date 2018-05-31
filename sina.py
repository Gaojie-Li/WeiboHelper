from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time
import random
import cookies
from datetime import datetime
import pickle
import os

emojis = []
with open("Data/emotions.txt",'r') as file:
    for line in file:
        emojis.append(line.strip())

def init_driver(ip="", port="", proxy=False,headless=False,driver="firefox"):

    incognito = True

    if driver == "firefox":
        #Firefox driver
        firefox_profile = webdriver.FirefoxProfile()
        firefox_profile.set_preference("browser.privatebrowsing.autostart", False)
        
        options = Options()
        if headless:
            options.add_argument('-headless')

        driver = webdriver.Firefox(firefox_profile=firefox_profile,firefox_options=options)
    else:
        #Chrome driver
        chrome_options = webdriver.ChromeOptions()
        if incognito:
            chrome_options.add_argument("--incognito")
        if headless:
            chrome_options.add_argument('--headless')
        if proxy:
            chrome_options.add_argument('--proxy-server=http://{0}:{1}'.format(ip, port))
            print('--proxy-server=http://{0}:{1}'.format(ip, port))

        driver = webdriver.Chrome(chrome_options=chrome_options)


    return driver


def readOnly(driver, tweets, freq, count):
    for i in range(count):
        print("="*20)
        print("READ ROUND {0}".format(i+1))
        tCount = 0
        for tweet_url in tweets:
            print("OPEN TWEET {0}".format(tCount+1))
            driver.get(tweet_url)
            wait_time = freq + random.randint(0,2)
            print("WAIT {0}s".format(wait_time))
            time.sleep(wait_time)
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

    openPage(driver, tweet_url)
    #randomly select a song
    lyrics_id = random.randint(0, len(lyrics)-1)
    print("SONG chosen: ", lyrics[lyrics_id])

    reposts = []
    
    #store previous lyrics as list object to save time reading lyrics file
    if os.path.exists(lyrics[lyrics_id].replace("txt","pkl")):
        reposts = pickle.load(open(lyrics[lyrics_id].replace("txt","pkl"), "rb"))
    else:
        with open(lyrics[lyrics_id],"r") as file:
            for line in file:
                reposts.append(line.strip())
        pickle.dump(reposts, open(lyrics[lyrics_id].replace("txt","pkl"),"wb"))

    repost(driver, tweet_url, reposts, comment=False, upper_bound=upper_bound)

#Repost with given repost messages
def repost(driver, tweet_url, reposts, comment=False, upper_bound=5):
    
    openPage(driver, tweet_url)
    
    repostCount = 0
    prev_selected = -1
    prev_repost_count = 0
    too_long = False
    while repostCount < upper_bound:
    # while repostCount < min(upper_bound, len(reposts)):
        try:
            print("{0}\tAttempting Repost({1})".format(str(datetime.now()),repostCount+1))
            print("="*20)
            if comment:
                btn = WebDriverWait(driver,10).until(lambda driver:driver.find_element_by_id("forward_comment_opt_forwardLi"))
                btm.click()
                # btn = driver.find_element(by=By.XPATH,value="//*[@id=\"forward_comment_opt_forwardLi\"]")
                # btn.click()
                # print("Skipping comment for now")

            repost_field, repost_btn, repost_message, repost_count = getRepostFields(driver)
            
            #Check if repost succeed
            if not too_long:
                if repost_count > prev_repost_count:
                    print("Repost succeed")
                    prev_repost_count = repost_count
                else:
                    print("Repost count didn't increase")
                    return


            i = repostCount % len(reposts)

            temp =  reposts[i] + emojis[random.randint(0,len(emojis)-1)] + repost_message + " "
            if post(driver, repost_field, repost_btn, temp,first = (repostCount == 0)):
                print("Repost({0}) Done".format(repostCount+1))
                print("="*20)
                repostCount += 1
                too_long = False
            else:
                del reposts[i]
                too_long = True

            driver.refresh()

        except Exception as e:
            print("\tERROR: ", str(e))



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

    repost_count = WebDriverWait(driver,10).until(lambda driver: driver.find_element(
        by=By.XPATH, 
        value="//*[@id=\"Pl_Official_WeiboDetail__73\"]/div/div/div/div[1]/div[4]/div[5]/div[2]/div[5]/div[1]/ul/li[1]/span/a/span/em[2]"))

    print("CURRENT REPOST COUNT: ", repost_count.get_attribute("innerHTML"))
    
    # rerepost_count = driver.find_element(by=By.XPATH,value="//*[@id=\"Pl_Official_WeiboDetail__73\"]/div/div/div/div[2]/div/ul/li[2]/a/span/span/span/em[2]")

    rerepost_count = WebDriverWait(driver, 10).until(lambda driver:driver.find_element(
        by=By.XPATH,value="//*[@id=\"Pl_Official_WeiboDetail__73\"]/div/div/div/div[2]/div/ul/li[2]/a/span/span/span/em[2]"))


    print("二转COUNT: ",rerepost_count.get_attribute("innerHTML"))
    repost_message = repost_field.get_attribute('value')
    # print(repost_message)
    return repost_field, repost_btn, repost_message, int(rerepost_count.get_attribute("innerHTML"))




def post(driver, repost_field, repost_btn, repost_message, first=False):
    if not first:
        sleep_time = max(1,5 + random.gauss(0,2))
        print("Cool Down for {0}s".format(sleep_time))
        time.sleep(sleep_time)
    if len(repost_message) > 140:
        handleRepostTooLong(repost_message)
        driver.refresh()
        return False
    repost_field.clear()
    time.sleep(5 + random.randint(0,2))
    repost_field.send_keys(repost_message)
    print("{0}\tRepost Message:\n\t{1}".format(str(datetime.now()),repost_message))
    repost_btn.click()
    time.sleep(2)

    driver.refresh()
    return True



def postOriginal(driver, post_message):
    driver.get("https://www.weibo.com")
    post_field = driver.find_element(by=By.XPATH,value="//*[@id=\"v6_pl_content_publishertop\"]/div/div[2]/textarea")
    post_btn = driver.find_element(by=By.XPATH, value="//*[@id=\"v6_pl_content_publishertop\"]/div/div[3]/div[1]/a")
    print("Make original posts")
    post_field.send_keys(post_message)
    time.sleep(5 + random.randint(0,2))
    post_btn.click()

    driver.refresh()
    return True

def search(driver):

    search_field=driver.find_element(by=By.XPATH,value="//*[@id=\"plc_top\"]/div/div/div[2]/input")
    search_field.send_keys("朱正廷")
    search_button = driver.find_element(by=By.XPATH, value="//*[@id=\"plc_top\"]/div/div/div[2]/a")
    search_button.click()
    time.sleep(5)
    driver.get("https://weibo.com/u/2949487607/home")

def handleRepostTooLong(message):
    print("\tERROR: Repost Message too long")
    print("\t"+message + "\n")
