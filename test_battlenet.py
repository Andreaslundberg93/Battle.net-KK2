from unittest import TestCase, main
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

class TestBattleNet(TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://eu.shop.battle.net/en-us?from=root")
        self.driver.maximize_window()
    
    def test_click_wow(self): 

        
        self.wowpage = self.driver.find_element(
            By.XPATH, "/html/body/storefront-root/storefront-standard-page-layout/storefront-home-page/div/main/div/storefront-contentstack-browsing-card-collection[1]/storefront-browsing-card-group/div/section/storefront-browsing-card-group-layout/ul/li[2]/storefront-browsing-card/div/storefront-link")
        self.assertEqual("Character Transfer", str)
        
    
    
    
    
    
    
    
    
    
    
    
    
    def tearDown(self):
        self.driver.delete_all_cookies()
        self.driver.quit()
    