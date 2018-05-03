import sina
from selenium import webdriver

users = {}
tweets = []
lyrics = []

test = True

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

with open("Data/MackDaddy.txt","r") as file:
    for line in file:
        lyrics.append(line.strip())

for u in users.keys():
    # sina.read(u, users[u], tweets)
    # sina.readOnly(tweets, 15, 30)
    sina.repost(u, users[u], tweets[1], lyrics, comment=False)
