import unittest
import time
import logging
from selenium import webdriver
from framework import page
from framework.locator import ConcertPageLocators
from selenium.webdriver.common.by import By

class ConcertSearch(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.stubbsaustin.com/")

    def test_grabConcertListings(self):
        #list = 
        """
        Grabs Concert Listings
        """
        main_page = page.MainPage(self.driver)
        assert main_page.is_title_matches(), "stubbsaustin title doesn't match assertion."
        main_page.click_concert_button()
        concert_results = page.ConcertPage(self.driver)
        listings = concert_results.bands_found()
        print(listings)
        time.sleep(5)

      

    #def tearDown(self):
       # self.driver.close()

if __name__ == "__main__":
    unittest.main()
