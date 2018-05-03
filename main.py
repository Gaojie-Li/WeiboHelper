import sina
from selenium import webdriver

users = {}
tweets = []

test = True

if test:
    config_file = "user_config_test.txt"
else:
    config_file = "user_config.txt"


with open(config_file,"r") as file:
    for line in file:
        line = line.strip().split("----")
        # print(line)
        users[line[0]] = line[1]

with open("tweets.txt","r") as file:
    for line in file:
        tweets.append(line.strip())



for u in users.keys():
    sina.read(u, users[u], tweets)
