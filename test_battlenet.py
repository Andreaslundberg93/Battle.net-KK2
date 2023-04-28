from unittest import TestCase, main
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class TestBattleNet(TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://eu.shop.battle.net/en-us?from=root")
        self.driver.maximize_window()
    
    def test_click_wow(self): 
        self.wowpage = self.driver.find_element(
            By.XPATH, "/html/body/storefront-root/storefront-standard-page-layout/div/storefront-navigation/div/storefront-desktop-nav/nav/div/div/div/storefront-dynamic-overflow-menu/ul/li[1]/meka-menu-drop-down/div/ul/li[1]/blz-nav-link//button/div").click()
        self.assertIn(self.driver.current_url)