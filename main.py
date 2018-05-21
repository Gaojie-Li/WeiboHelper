import sina
import cookies
from selenium import webdriver
import os
import random
import argparse


def read_config(test=False):
    if test:
        config_file = "config_test.txt"
    else:
        config_file = "config.txt"

    users = {}
    with open(config_file,"r") as file:
        for line in file:
            line = line.strip().split("----")
            # print(line)
            users[line[0]] = line[1]

    return users


def read_repost_messages(repost_lyrics=False):
    reposts = []
    if repost_lyrics:
        if os.path.exists("lyrics.list"):
            os.system("rm lyrics.list")
        os.system("for t in lyrics/*.txt; do greadlink -f $t>>lyrics.list;done;")

        with open("lyrics.list","r") as file:
            for line in file:
                reposts.append(line.strip())
    else:
        with open("Data/zztJinghua.txt", "r") as file:
            for line in file:
                reposts.append(line.strip())


    originals = []
    with open("Data/originalPost.txt","r") as file:
        for line in file:
            originals.append(line.strip())
    return reposts, originals

def read_tweets():
    tweets = []
    with open("Data/tweets.txt","r") as file:
        for line in file:
            tweets.append(line.strip().split("\t")[0])
    return tweets


def read_ip():
    ips = []
    with open("ip.list","r") as file:
        for line in file:
            line = line.strip().split("\t")
            # if line[-2] != "yes":
            #     continue
            ips.append(line[:2])
            # print(ips)
    return ips


def readZZT():
    zzt_tweets=[]
    with open("Data/zzt_tweets.txt","r") as file:
        for line in file:
            zzt_tweets.append(line.strip())
        print(zzt_tweets)
    cookies.saveCookies("0018582636158", "Lunar214")
    driver = cookies.loadCookies("0018582636158",ip="", port="", proxy=False)
    sina.readOnly(driver, zzt_tweets, 20, 1000)


def main():
    parser = argparse.ArgumentParser(description="Automatic Repost Script")
    parser.add_argument('--read',default=False,help="刷阅读量否")
    parser.add_argument('--lyrics',default=True,help="唱歌否")
    parser.add_argument("--comment",default=True,help="勾选评论否")
    parser.add_argument("--search",default=False,help="刷搜索量否")
    parser.add_argument("--upper_bound",default=10,type=int,help="转发上限")
    parser.add_argument("--headless",default=False,help="无头否")
    args=parser.parse_args()


    users = read_config(test=True)

    read = args.read
    if read:
        readZZT()


    test = True
    repost_lyrics = args.lyrics
    comment = args.comment
    search = args.search
    headless = args.headless

    print("Repost Settings:")
    print("刷阅读量否:{0}".format(args.read))
    print("唱歌否:{0}".format(args.lyrics))
    print("勾选评论否:{0}".format(args.comment))
    print("刷搜索量否:{0}".format(args.search))
    print("转发上限:{0}".format(args.upper_bound))
    print("无头否:{0}".format(args.headless))

    tweets = read_tweets()
    reposts, originals = read_repost_messages(repost_lyrics)
    upper_bound = args.upper_bound

    uCount = 0
    try:
        for u in users.keys():
            newly_saved, driver = cookies.saveCookies(u, users[u],headless=headless)

            if not newly_saved:
                driver = cookies.loadCookies(u,headless=headless)
            
            print(driver.current_url)
            if "home" in driver.current_url:
                print("登陆成功")
            else:
                driver.quit()
                newly_saved, driver = cookies.saveCookies(u, users[u],force=True)
            # sina.read(u, users[u], tweets)
            # sina.readOnly(tweets, 15, 30)


            #Make reposts

            print("Upper Bound: {0}".format(upper_bound))
            if repost_lyrics:
                sina.repostLyrics(driver, tweets[-1], reposts, comment=comment, upper_bound=upper_bound)
            else:
                reposts = random.shuffle(reposts)
                sina.repost(driver, tweets[-1], reposts, comment=comment, upper_bound=upper_bound)

            #Make original post after reposts
            sina.postOriginal(driver, originals[random.randint(0,len(originals)-1)])
            uCount += 1

            if search:
                #Search five times
                for _ in range(5):
                    sina.search(driver)
                    print("search {0}".format(_))

            driver.quit()

            print("-----close browser-----")
    except Exception as e:
                    print("Error: ", str(e))

if __name__ == '__main__':
    main()
