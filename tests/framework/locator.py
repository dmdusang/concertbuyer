from selenium.webdriver.common.by import By

class MainPageLocators(object):
    
    CONCERT_BUTTON = (By.LINK_TEXT, 'Concert Listings')

class ConcertPageLocators(object):
    CONCERT_BLOCK = (By.NAME, 'contentTitle')
    BAND_NAME = (By.CSS_SELECTOR, 'itemprop="url"')