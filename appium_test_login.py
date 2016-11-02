import os
import unittest
import random
from appium import webdriver
from time import sleep

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class Util(object):

	def random_num(self, num):
		phone = '';
		for x in range(0, num):
			phone = phone + str(random.randrange(0, 10));
		return phone

class AndroidTests(unittest.TestCase):
    def random_phone(self):
        phone = "";
        for x in range(1,10):
            phone = phone + random.randrange(0, 10);
        return phone


    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['appPackage'] = 'com.lt7.lt'
        desired_caps['appActivity'] = 'com.luckin.magnifier.activity.account.LoginActivity'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_to_login(self):
        
        util = Util()

        textfields = self.driver.find_elements_by_class_name("android.widget.EditText")
        textfields[0].send_keys(util.random_num(11))
        textfields[1].send_keys(util.random_num(6))

        self.driver.find_element_by_id("login").click()

        # for some reason "save" breaks things
        alert = self.driver.switch_to_alert()

        # no way to handle alerts in Android
        self.driver.find_element_by_android_uiautomator('new UiSelector().clickable(true)').click()

        # self.driver.press_keycode(3)

    


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)

