from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


from lxml import html
import requests
import json
import re


import matplotlib.pyplot as plt
#adopted from https://www.jianshu.com/p/cc72f42ee0cb

# 获取指定博主的所有微博card的list
def getWeibo(id,page):#id（字符串类型）：博主的用户id，page（整型）：微博翻页参数

    url='https://m.weibo.cn/api/container/getIndex?type=uid&value='+id+'&containerid=107603'+id+'&page='+str(page)
    # print(url)
    response=requests.get(url)
    ob_json=json.loads(response.text)
    # print(ob_json.keys())
    # print(ob_json['data']['cards'])

    list_cards=ob_json['data']['cards']
    return list_cards# 返回本页所有的cards


# cards = getWeibo("2949487607",1)
#2447034645 <-是贝贝的user id
i = 1
weibo_count = 1
cards = getWeibo('2447034645',i)
reposts = []
comments = []
while len(cards) != 0:
	for c in cards:
		# print(c)
		# print(c['card_type'])
		if c['card_type'] == 9:
			print("WEIBO {0}".format(weibo_count))
			print(c['mblog']['text'])

			reposts.append(c['mblog']['reposts_count'])
			comments.append(c['mblog']['comments_count'])


			print("转发：",reposts[-1])
			print("评论：",comments[-1])
			print("点赞：",c['mblog']['attitudes_count'])
			weibo_count += 1
		# print(c['card_type'])

		# print(c)
			print("-"*10)
	i += 1
	cards = getWeibo('2447034645',i)
	
#TODO: 有三条wb不知所踪了不知道为啥爬不下来
