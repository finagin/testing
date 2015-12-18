# -*- coding: utf-8 -*-
import unittest, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class MyHelper:
    def __init__(self, driver="Firefox"):
        driver = getattr(webdriver, driver)
        if callable(driver):
            self.driver = driver()

    def open(self, url):
        self.driver.get(url)

    def auth(self, login, password):
        time.sleep(0.5)
        login_el = self.driver.find_element_by_id('id_username')
        login_el.clear()
        login_el.send_keys(login)

        time.sleep(0.5)
        password_el = self.driver.find_element_by_id('id_password')
        password_el.clear()
        password_el.send_keys(password)
        password_el.send_keys(Keys.RETURN)

    def create_issues(self, title, description):
        title_el = self.driver.find_element_by_id('id_title')
        title_el.clear()
        title_el.send_keys(title)

        time.sleep(0.5)
        description_el = self.driver.find_element_by_id('id_content')
        description_el.clear()
        description_el.send_keys(description)

        time.sleep(0.5)
        self.driver.find_element_by_css_selector('#issues .aui-button.aui-button-primary').click()
