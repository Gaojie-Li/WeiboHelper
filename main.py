import sina
from selenium import webdriver

users = {}
tweets = []

test = False

if test:
    config_file = "config.txt"
else:
    config_file = "config.txt"


with open(config_file,"r") as file:
    for line in file:
        line = line.strip().split("----")
        # print(line)
        users[line[0]] = line[1]

with open("tweets.txt","r") as file:
    for line in file:
        tweets.append(line.strip())



for u in users.keys():
    # sina.read(u, users[u], tweets)
    sina.readOnly(tweets, 15, 30)
