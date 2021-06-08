import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select

class LangugeOptions(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = 'C:/Users/Jesus David Gomez\Documents/Platzi/Curso de Introducción a Selenium con Python/chromedriver_win32/chromedriver.exe')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com/')


    def test_select_language(self):
        exp_options = ['English', 'French', 'German']
        act_options = []

        select_languge = Select(self.driver.find_element_by_id('select-language'))

        self.assertEqual(3, len(select_languge.options))

        for option in select_languge.options:
            act_options.append(option.text)

        self.assertListEqual(exp_options, act_options)

        self.assertEqual('English', select_languge.first_selected_option.text)

        select_languge.select_by_visible_text('German')

        self.assertTrue('store=german' in self.driver.current_url)

        select_languge = Select(self.driver.find_element_by_id('select-language'))
        select_languge.select_by_index(0)


    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.close()


if __name__ == '__main__':
    unittest.main(verbosity = 2)