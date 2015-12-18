# -*- coding: utf-8 -*-

import unittest, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from helpers import *
from data_creator import *


class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        DataCreator('data', 'finagin', 'z123z123')
        self.data = DataRead('data')
        self.helper = MyHelper()

    def test_search_in_python_org(self):
        self.helper.open('https://bitbucket.org/poachers/gitpard-old/issues/new')
        i = 0
        while i != -1:
            print i
            temp = self.data.data['auth'][i]
            print temp
            time.sleep(1)
            try:
                self.helper.auth(temp['login'], temp['password'])
                assert "Invalid username/email or password." not in self.helper.driver.page_source, u'ОШИБКА'
                i = -1
            except:
                i += 1
                print i

        self.helper.create_issues(self.data.data["issues"]["title"], self.data.data["issues"]["description"])

        # helper.driver.close()
        # driver = self.driver
        # driver.get("http://vk.com")
        # # self.assertIn("Python", driver.title)
        #
        # login = driver.find_element_by_id('quick_email')
        # password = driver.find_element_by_id('quick_pass')
        # button = driver.find_element_by_id('quick_login_button')
        #
        # login.send_keys(u"+79179360087")
        # password.send_keys(u'skdngslgnslreg')
        # button.click()
        #
        # time.sleep(3)
        #
        # driver = self.driver
        # driver.get("http://vk.com")
        # # self.assertIn("Python", driver.title)
        #
        # login = driver.find_element_by_id('quick_email')
        # password = driver.find_element_by_id('quick_pass')
        # button = driver.find_element_by_id('quick_login_button')
        #
        # login.send_keys(u"+79179360087")
        # password.send_keys(u'НеТрогайМойВк!11')
        # button.click()
        #
        # time.sleep(5)
        #
        # post = driver.find_element_by_id('post_field')
        # send_post = driver.find_element_by_id('send_post')
        # post.send_keys(u'Ебать как я люблю тестинг!!')
        # send_post.click()

        # ============================================================
        # ============================================================

        # form = driver.find_element_by_class_name('signin')
        # login = driver.find_element_by_id('signin-email')
        # password = driver.find_element_by_id('signin-password')
        # submit = driver.find_element_by_id('signin-password')
        #
        # login.send_keys("IgorFinagin")
        # assert "No results found." not in driver.page_source
        # login.send_keys(Keys.RETURN)
        # password.send_keys("z123x123c123")
        # assert "No results found." not in driver.page_source
        # password.send_keys(Keys.RETURN)
        # form.submit()

        # assert "No results found." not in driver.page_source
        # elem.send_keys(Keys.RETURN)

    def tearDown(self):
        self.helper.driver.close()


if __name__ == "__main__":
    unittest.main()
