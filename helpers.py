# -*- coding: utf-8 -*-
import unittest, time, decorators
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class MyHelper:
    def __init__(self, driver="Firefox"):
        driver = getattr(webdriver, driver)
        if callable(driver):
            self.driver = driver()

    def open(self, url):
        self.driver.get(url)
        self.driver.maximize_window()

    @decorators.mc_sleep(2000)
    def fill_field_by_id(self, id, text, enter=False):
        element = self.driver.find_element_by_id(id)
        element.clear()
        element.send_keys(text)
        if enter:
            element.send_keys(Keys.RETURN)

    @decorators.mc_sleep(4000)
    def click_by_id(self, id):
        self.driver.find_element_by_id(id).click()

    def auth(self, login, password):
        apply(self.fill_field_by_id, login)
        apply(self.fill_field_by_id, password)

    def auth_with_data(self, data):
        try:
            self.auth(['id_username', data['login']], ['id_password', data['password'], True])
            assert "Invalid username/email or password." not in self.driver.page_source, u'ОШИБКА'
            return True
        except:
            return False

    # @decorators.mc_sleep(400)
    def logout(self):
        self.click_by_id('repo-issues-link')
        self.click_by_id('user-dropdown-trigger')
        self.click_by_id('log-out-link')

    def create_issues(self, data):
        ts = time.strftime('%d/%m/%Y %H:%M:%S')
        apply(self.fill_field_by_id, ['id_content', data['description']])
        apply(self.fill_field_by_id, ['id_title', ts + ' | ' + data['title'], True])
        return ts
    @decorators.mc_sleep(5000)
    def resolve_issue(self, data):
        print "//*[contains(text(), '" + data['title'] + "')]"
        self.driver.find_elements_by_xpath("//*[contains(text(), '" + data['title'] + "')]")[0].click()
        self.click_by_id('change-state')
        self.driver.find_element_by_id('issue-transition-form').submit()
