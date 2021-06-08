import unittest
from selenium import webdriver


class Typos(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r"C:/Users/Jesus David Gomez\Documents/Platzi/Curso de Introducción a Selenium con Python/chromedriver_win32/chromedriver.exe")
        driver = self.driver
        driver.get("http://the-internet.herokuapp.com/")
        driver.find_element_by_link_text('Typos').click()


    
    def test_find_typo(self):
        drive = self.driver

        paragraph_to_check = drive.find_element_by_css_selector('#content > div > p:nth-child(3)')
        text_to_check = paragraph_to_check.text
        print(text_to_check)

        tries = 1
        found = False
        correct_text = "Sometimes you'll see a typo, other times you won't."

        while text_to_check != correct_text:
            paragraph_to_check = drive.find_element_by_css_selector('#content > div > p:nth-child(3)')
            text_to_check = paragraph_to_check.text
            drive.refresh()

        while not found:
            if text_to_check == correct_text:
                tries += 1
                drive.refresh
                found = True

        self.assertEqual(found, True)

        print(f'It took {tries} tries to find the typo')


    
    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()