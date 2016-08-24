import logging
import os
import unittest

import time

import re

import sys
from appium import webdriver

# Returns abs path relative to this file and not cwd


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class SimpleAndroidTests(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['app'] = PATH(
            'iov_final_1.apk'
        )

        self.driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)

    def tearDown(self):
        # end the session
        self.driver.quit()

    tan = 0

    def test_find_elements(self):
        #log = logging.getLogger('test_find_elements')
        bankpin = self.driver.find_element_by_id("com.iov.iov42:id/etBankPin_AA")
        bankpin.click()
        bankpin.send_keys('445755889')

        psw = self.driver.find_element_by_id("com.iov.iov42:id/etPassword_AA")
        bankpin.click()
        psw.send_keys('445755889')
        time.sleep(1)
        #self.driver.hide_keyboard()
        #self.driver.back()
        #time.sleep(5)
        self.driver.keyevent(4)
        time.sleep(3)
        checkbox = self.driver.find_element_by_id("com.iov.iov42:id/cbAgreement_AA")
        checkbox.click()


        time.sleep(2)
        refreshButton = self.driver.find_element_by_id("com.iov.iov42:id/btPinLogIn_AA")
        self.assertTrue(refreshButton.is_displayed())
        refreshButton.click()

        time.sleep(3)

        notif = self.driver.open_notifications()
        time.sleep(2)

        all = self.driver.find_elements_by_id("android:id/text")
        tan = []
        for a in all:
            #a = a.strip()
            if "TAN Number" in a.text:

                tan += re.findall(r'\d+', a.text, flags=0)

            else:
                return logging.getLogger().info("TAN wasn't send")
            tan.append(tan)
        time.sleep(1)
        #self.driver.switch_to_window()
        #---------------------------------------------
        time.sleep(2)
        self.driver.keyevent(4)
        tan_field = self.driver.find_element_by_id("com.iov.iov42:id/etTan_AA")
        tan_field.click()
        tan_field.send_keys(tan[0])
        #---------------------------------------------
        time.sleep(2)
        self.driver.keyevent(4)
        #---------------------------------------------
        time.sleep(1)
        login = self.driver.find_element_by_id("com.iov.iov42:id/btTanLogIn_AA")
        time.sleep(1)
        login.click()
        time.sleep(3)


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stderr)
    logging.getLogger("SomeTest.testSomething").setLevel(logging.DEBUG)
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
