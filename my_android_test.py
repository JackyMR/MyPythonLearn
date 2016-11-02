#coding:utf-8
import os
import HTMLTestRunner
import unittest
from selenium import webdriver

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class elementA(unittest.TestCase):	
	def test_(self):	
		desired_caps = {}
		desired_caps['deviceName'] = '192.168.39.101:5555'  #adb devices查到的设备名
		desired_caps['platformName'] = 'Android'
		desired_caps['platformVersion'] = '5.1'		
		desired_caps['appPackage'] = 'com.lt7.lt'  #被测App的包名
		desired_caps['appActivity'] = 'com.luckin.magnifier.activity.account.LoginActivity' #启动时的ActPivity
		driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
	def test_login(self ):
		ph = driver.find_element_by_id("et_phone_number")
		self.assertIsNotNone(ph)
		ph.send_keys("18939517624")		
		ps = driver.find_element_by_id("et_password")
		self.assertIsNotNone(ps)
		ps.send_keys("qwerty")
		lg = driver.find_element_by_id("login")
		self.assertIsNotNone(lg)
		lg.click()
		
	
if __name__ == '__main__':
    testunit=unittest.TestSuite()        #定义一个单元测试容器
    testunit.addTest(elementA("test_"))  #将测试用例加入到测试容器中    
    filename="./myAppiumLog.html"        #定义个报告存放路径，支持相对路径。
    fp=file(filename,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='Report_title',description='Report_description')  #使用HTMLTestRunner配置参数，输出报告路径、报告标题、描述
    runner.run(testunit)                 #自动进行测试