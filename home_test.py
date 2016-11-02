import os
import unittest
from appium import webdriver
from time import sleep

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

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
        desired_caps['appActivity'] = 'com.luckin.magnifier.activity.MainActivity'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_to_login(self):
        
        # self.driver.find_element_by_id("btn_holding_advertising_close").click()

        listviews = self.driver.find_elements_by_class_name("android.widget.ListView")
        
        item = listviews[0].find_elements_by_class_name("android.widget.LinearLayout")
        item[2].click()



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)

