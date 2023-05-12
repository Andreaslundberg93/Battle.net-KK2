from selenium import webdriver 
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By 
import unittest 
from selenium.webdriver.common.action_chains import ActionChains 
import time 

class InetTest(unittest.TestCase): 
    
    @classmethod 
    def setUpClass(cls): 
        cls.driver = webdriver.Chrome() 
        cls.driver.implicitly_wait(10) 
        cls.driver.maximize_window() 
        
    def setUp(self):
        self.driver.get("https://inet.se") 
            
    def test_datorkomponenter(self):
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div[7]/div/button[1]").click() 
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/div[2]/div[2]/div[3]/a[2]").click() 
        datorkomponenter = self.driver.find_element(By.XPATH , "/html/body/div[1]/div[3]/div/div/div[2]/div[2]/section/h1")
        self.assertTrue(datorkomponenter.is_displayed)
        
    def test_add_cart(self):
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div[7]/div/button[1]").click()
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div/div/div[2]/div[2]/div[12]/div/div/div[1]/a').click()
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div/div/div[2]/div[2]/article/div[8]/div[1]/div/section/div[4]/div/button').click()
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/nav/div/div/div[6]/div/div/div/a').click()
        vara = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[2]/div/div/div/ul/li/div/article/div[1]/div[1]/a')
        self.assertTrue(vara.is_displayed)
        
    def test_verify_malmo_address(self):
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div[7]/div/button[1]").click()
        self.driver.find_element(By.XPATH, "/html/body/div[1]/footer/div/section[1]/article[1]/ul/li[4]/a").click()
        correct_adress = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/div[2]/div[2]/cms-content/article/cms-content/div/div[4]/div[1]/h2/small")
        self.assertTrue(correct_adress.is_displayed)
        
    def test_verify_kundservice_oppettider_vardagar(self):
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div[7]/div/button[1]").click()
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/div[1]/section/a[2]").click()
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/div[2]/div[2]/cms-content/article/cms-content/div[2]/div[6]/a").click()
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/div[1]/section/a[2]").click()
        oppettider_vardag = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/div[2]/div[2]/cms-content/article/cms-content/div/div/div[2]/div[1]/div[2]/table/tbody/tr[1]/td[2]")
        self.assertTrue(oppettider_vardag.is_displayed)
        
    def test_select_specific_product_brand(self):
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div[7]/div/button[1]").click()
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/div[1]/div/div[2]/ol/li[3]/div/button").click()
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/div[1]/div/div[2]/ol/li[3]/div[2]/div/ol/li[3]/div/button").click()
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/div[1]/div/div[2]/ol/li[3]/div[2]/div/ol/li[3]/div[2]/div/ol/li[6]/div/button").click()
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/div[1]/div/div[2]/ol/li[3]/div[2]/div/ol/li[3]/div[2]/div/ol/li[6]/div[2]/div/ol/li[4]/a").click()
        correct_specific_product = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/div[2]/div[2]/section/div/div[2]/div[2]/ul/li/div/a/h4")
        self.assertTrue(correct_specific_product.is_displayed)
    def tearDown(self): 
        self.driver.delete_all_cookies() 
        
        
    @classmethod 
    def tearDownClass(cls): 
        cls.driver.quit()