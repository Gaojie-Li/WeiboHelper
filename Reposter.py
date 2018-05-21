from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random
import cookies
from datetime import datetime


class Reposter:
	driver = webdriver.Chrome()

	def isVerifyCodeExist(self):
		try:
			# 如果成功找到验证码输入框返回true
			self.driver.find_element_by_css_selector('input[name="verifycode"]')
			return True
		except:# 如果异常返回false
			return False

		# 输入验证码部分，如果无需输入则直接返回，否则手动输入成功后返回
	def inputVerifyCode(self):
	   input_verifycode=self.driver.find_element_by_css_selector('input[name="verifycode"]')# 验证码输入框
	   bt_change=self.driver.find_element_by_css_selector('img[action-type="btn_change_verifycode"]')# 验证码图片，点击切换
	   bt_logoin=self.driver.find_element_by_class_name('login_btn')# 登录按钮
	   while self.isVerifyCodeExist():
		   print(u'请输入验证码……(输入"c"切换验证码图片)')
		   verifycode=input()
		   if verifycode=='c':
			   bt_change.click()
		   else:
			   input_verifycode.send_keys(verifycode)
			   bt_logoin.click()
			   # 点击完登录以后判断是否成功
			   time.sleep(5)
			   if self.driver.current_url.split('/')[-1]=='home':
				   print(u'登录成功')
				   break
			   else:
				   print(u'输入的验证码不正确')

	#打开微博首页进行登录的过程
	def login(self,account,password):
		self.driver.implicitly_wait(10)# 设置隐性等待时间，等待页面加载完成才会进行下一步，最多等待10秒
		url='http://weibo.com/'
		self.driver.get(url)
		#输入账号密码并登录
		time.sleep(10)
		username_fd = self.driver.find_element(by=By.ID, value="loginname")
		password_fd = self.driver.find_element(By.NAME, value="password")

		username_fd.send_keys(account)
		password_fd.send_keys(password)

	   # WebDriverWait(self.driver,10).until(lambda x:x.find_element_by_id('loginname')).send_keys(account)
	   # self.driver.find_element_by_css_selector('input[type="password"]').send_keys(password)

		bt_logoin=self.driver.find_element_by_class_name('login_btn')
		bt_logoin.click()

		#如果存在验证码，则进入手动输入验证码过程
		if self.isVerifyCodeExist():
			self.inputVerifyCode()
