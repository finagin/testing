# -*- coding: utf-8 -*-

import unittest, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from helpers import *
from data_creator import *
from decorators import *


class PythonOrgSearch(unittest.TestCase):

    data = DataCreator('data', 'finagin', 'z123z123')

    def setUp(self):
        self.logins = 3
        self.helper = MyHelper()

    def test_create_issue(self):
        helper = self.helper

        helper.open('https://bitbucket.org/poachers/gitpard-old/issues/new')

        i = 0
        auth = helper.auth_with_data(DataRead('data').auth(i))
        while not auth and i < self.logins:
            i += 1
            auth = helper.auth_with_data(DataRead('data').auth(i))

        # try:
        assert auth, 'Не удалось авторизоваться'
        # except:
        #     helper.driver.close()

        helper.create_issues(DataRead('data').issue())

        # try:
        assert time.strftime('%d/%m/%Y %H') in helper.driver.page_source, 'Не удалось запостить issue'
        # except:
        #     helper.driver.close()

        helper.logout()

        helper.driver.close()

    def test_resolve_issue(self):
        helper = self.helper

        helper.open('https://bitbucket.org/poachers/gitpard-old/issues')

        auth = helper.auth_with_data(DataRead('data').auth(self.logins))

        assert auth, 'Не удалось авторизоваться'

        helper.resolve_issue(DataRead('data').issue())

        assert "RESOLVED" not in self.driver.page_source, u'ОШИБКА'

        helper.logout()

    def tearDown(self):
        self.helper.driver.close()


if __name__ == "__main__":
    unittest.main()
