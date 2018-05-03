from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def read(uname, upass, tweets):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    # chrome_options.add_argument('--headless')
    chrome_options.add_argument('--proxy-server=http://39.134.68.22:80')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.set_window_size(600,500)

    driver.get('http://httpbin.org/ip')
    print(driver.page_source)


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


    # safe_login.click()
    # time.sleep(2)
    smb_btn.click()
    time.sleep(5)

    # tweet_url = "https://weibo.com/2858423732/G8fr3hR3E?from=page_1005052858423732_profile&wvr=6&mod=weibotime&type=repost"

    # driver.findElement(By.cssSelector("body")).sendKeys(Keys.CONTROL +"t");
    # driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
    #
    # time.sleep(5)
    i = 0

    #try opening new tweets one after another
    for tweet_url in tweets:
        print("open new tweet {0}".format(i+1))
        driver.get(tweet_url)
        time.sleep(15)
        i += 1



    #try opening multiple tabs
    # for tweet_url in tweets:
    #     print("open new tweet {0}".format(i+1))
    #     driver.execute_script("window.open()")
    #     driver.switch_to.window(driver.window_handles[-1])
    #     driver.get(tweet_url)
    #     i += 1
    # time.sleep(15)


    driver.quit()

    print("-----close browser-----")

    # #check forward and comment
    # btn = driver.find_element_by_id("forward_comment_opt_forwardLi")
    # #TODO: how to get the textbox???
    # btn.click()

    # text = driver.find_element_by_title('转发微博内容')
    # text.send_keys(u'\u8f6c\u53d1\u62bd\u5956')
    #
    # forward_btm = driver.find_element_by_xpath("//[@type='submit']")
    # forward_btm.click()


    # btn = driver.find_element_by_class_name("W_ficon.ficon_forward.S_ficon")
    # btn.click()


    # btm = driver.find_element_by_class_name("W_ficon")
    # btm.click()
    #

    # text = driver.find_element_by_id('p_input')
    # text = driver.find_element_by_xpath("//W_input[@node-type='textEl']")
    # text = driver.find_element_by_id("")
    # textbox = driver.find_element_by_xpath("//W_input")
    # for t in textbox:
    #     t.send_keys("1")
    # text.send_keys("1")
    # send=driver.find_element_by_xpath("//input[@type='submit']")
    # send.click()
    # time.sleep(5)

    # text = driver.find_element_by_id('content')
    # text.send_keys(u'\u8f6c\u53d1\u62bd\u5956')
    # time.sleep(5)
    # send = driver.find_element_by_xpath("//input[@type='submit']")
    # send.click()
    # time.sleep(5)
    # driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'w')
    # time.sleep(1)

    # tweet_url = "https://weibo.cn/2858423732/4219659614255534"
