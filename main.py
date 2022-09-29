import time
import unittest

import Variables.GlobalVariables as gv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Common.Find import CustomFind

class TestCase(unittest.TestCase):
    def setUp(self):
        #preconditions part
        self.driver = webdriver.Chrome("Drivers/chromedriver.exe")
        self.driver.maximize_window()
        self.driver.delete_all_cookies()
        self.driver.implicitly_wait(10)
        self.find = CustomFind(self.driver)
        self.driver.get(gv.amazonURL)

    def test_amazon_sinple(self):
        searchField = self.find.custom_find_element((By.ID, "twotabsearchtextbox"))
        searchField.clear()
        searchField.send_keys("AGV Helmet")
        searchField.send_keys(Keys.ENTER)

        # productFromSearchResultPage = driver.find_element(By.XPATH, "(//span[@class='a-size-base a-color-base a-text-normal'])[1]")
        productFromSearchResultPage = self.find.custom_find_element((By.XPATH, "(//span[@class='a-size-base a-color-base a-text-normal'])[1]"))
        productFromSearchResultPage.click()

    def tearDown(self):
        self.driver.close()
