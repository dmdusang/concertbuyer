from framework.element import BasePageElement
from framework.locator import MainPageLocators
from framework.locator import ConcertPageLocators
import logging

class SearchTextElement(BasePageElement):
    """This class gets the search text from the specified locator"""

    #The locator for search box where search string is entered
    locator = 'q'


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):

    #Declares a variable that will contain the retrieved text
    search_text_element = SearchTextElement()

    def is_title_matches(self):
        return "Stubb's BBQ" in self.driver.title

    def click_concert_button(self):
        element = self.driver.find_element(*MainPageLocators.CONCERT_BUTTON)
        element.click()


class ConcertPage(BasePage):

    def bands_found(self):
        # Search for bands and return array
        #bands = []
       for band in self.driver.find_elements(*ConcertPageLocators.CONCERT_BLOCK):
            #locate logic
            print(band)
            logging.info(band)
            name = band.find_element(*ConcertPageLocators.BAND_NAME).text
            
            bands.append(name)
        bands = self.driver.find_elements(*ConcertPageLocators.CONCERT_BLOCK)
        return bands

