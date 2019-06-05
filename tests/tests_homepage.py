import unittest
from selenium import webdriver


class HomePage(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        #create new Chrome session
        inst.driver = webdriver.Chrome()
        inst.driver.implicitly_wait(10)
        inst.driver.maximize_window()
        #navigate to the application home page
        inst.driver.get("http://www.google.com")
        inst.driver.title

    def test_search_by_text(self):
        self.search_field = self.driver.find_element_by_name("q")
        self.search_field.clear()
        #enter search keyword and submit
        self.search_field.send_keys("Selenium Webdriver interview questions")
        self.search_field.submit()
        #get the list of elements which are displayed after the search
        #currently on result page using find_elements_by_class_name method
        lists = self.driver.find_elements_by_class_name("r")
        self.assertEqual(14,len(lists))


    def check_page_exists(self):
        self.driver.find_element_by_id("hplogo")


    @classmethod
    def tearDownClass(inst):
        #close browser window
        inst.driver.close()
        inst.driver.quit()

if __name__ == '__main__':
    unittest.main()