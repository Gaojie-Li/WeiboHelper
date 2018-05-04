import sina
import cookies
from selenium import webdriver
import os

users = {}
tweets = []
lyrics = []
reposts = []
ips = []

test = True
repost_lyrics = False

if test:
    config_file = "config_test.txt"
else:
    config_file = "config.txt"


with open(config_file,"r") as file:
    for line in file:
        line = line.strip().split("----")
        # print(line)
        users[line[0]] = line[1]

with open("Data/tweets.txt","r") as file:
    for line in file:
        tweets.append(line.strip())


if repost_lyrics:
    if os.path.exists("lyrics.list"):
        os.system("rm lyrics.list")
    os.system("for t in lyrics/*.txt; do greadlink -f $t>>lyrics.list;done;")

    with open("lyrics.list","r") as file:
        for line in file:
            lyrics.append(line.strip())
else:
    with open("Data/zztRepost.txt", "r") as file:
        for line in file:
            reposts.append(line.strip())

with open("ip.list","r") as file:
    for line in file:
        line = line.strip().split("\t")
        # if line[-2] != "yes":
        #     continue
        ips.append(line[:2])
        # print(ips)

uCount = 0
for u in users.keys():
    cookies.saveCookies(u, users[u],ip=ips[uCount][0], port=ips[uCount][1], proxy=False)
    driver = cookies.loadCookies(u, ip=ips[uCount][0], port=ips[uCount][1], proxy=False)
    # sina.read(u, users[u], tweets)
    # sina.readOnly(tweets, 15, 30)
    if repost_lyrics:
        sina.repostLyrics(driver, tweets[-1], lyrics, comment=True)
    else:
        sina.repost(driver, tweets[-1], reposts, comment=True)
    uCount += 1
