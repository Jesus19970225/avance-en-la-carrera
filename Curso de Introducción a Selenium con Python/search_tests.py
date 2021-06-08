import unittest
from selenium import webdriver

class SearchTests(unittest.TestCase):

    def setUp(self):
	    self.driver = webdriver.Chrome(executable_path = r'C:/Users/Jesus David Gomez\Documents/Platzi/Curso de Introducción a Selenium con Python/chromedriver_win32/chromedriver.exe')
	    driver = self.driver
	    driver.implicitly_wait(30)
	    driver.maximize_window()
	    driver.get("http://demo-store.seleniumacademy.com/")


    def test_search_tee(self):
        driver = self.driver
        search_field = driver.find_element_by_name('q')
        search_field.clear()

        search_field.send_keys('tee')
        search_field.submit()
        

    def test_search_salt_shaker(self):
	    driver = self.driver
	    search_field = driver.find_element_by_name('q')
		
	    search_field.send_keys('salt shaker') #escribimos 'salt shaker' en la barra de búsqueda
	    search_field.submit() #envíamos la petición

		#hago una lista de los resultados buscando los elementos por su Xpath. Es la forma más rápida.
	    products = driver.find_elements_by_xpath('//*[@id="top"]/body/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/ul/li/div/h2/a')

		#vamos a preguntar si la cantidad de resultados es igual a 1
	    self.assertEqual(1, len(products))
	
		
    def tearDown(self):
	    self.driver.quit()