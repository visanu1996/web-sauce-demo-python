import unittest
from selenium import webdriver
import os
import time
from utils.logger import get_logger
from resource.common import Common

from resource.POM.login import *
from resource.POM.product import *
from resource.POM.cart import *

class TestSauceDemo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        conf_path = os.path.join(project_root,'testdata','config.yml')
        
        
        cls.logger = get_logger(__name__)
        cls.common = Common(cls.driver)
        cls.config = cls.common.read_yml(conf_path)
        
        try:
            open_browser_with_url(cls.driver,cls.config.get("SAUCE_URL"))
            cls.driver.maximize_window()
            cls.logger.info('Open browser successfully.')
            
        except Exception as e:
            cls.logger.error(f"Error after trying to open browser: {e}")
            raise
    
    # def setUp(self):
        # self.common.driver.refresh()  # Fully reloads the login page
        # time.sleep(2)
        
    @classmethod
    def tearDownClass(cls):
        if hasattr(cls,'driver') and cls.driver:
            cls.driver.close()
            cls.logger.info("Webdriver closed.")
    
    # def test_001_login_no_username(self):
    #     ''' test login no username '''
    #     self.logger.info("Step: Attempt login with no username")
    #     fill_username_password(self.common,None,PASSWORD)
    #     self.common.verify_text_contains(By.XPATH,LOGIN_PAGE_LOCATOR['toast'],ERROR['user_req'])
    #     time.sleep(5)    
    
    # def test_002_login_no_password(self):
    #     ''' test login no password '''
    #     self.common.driver.refresh()  # Fully reloads the login page
    #     time.sleep(2)    
    #     self.logger.info("Step: Attempt login with no password")
    #     fill_username_password(self.common,USERNAME["std"],None)
    #     self.common.verify_text_contains(By.XPATH,LOGIN_PAGE_LOCATOR['toast'],ERROR['pass_req'])
    #     time.sleep(5)       
    
    # def test_003_login_invalid_credentials(self):
    #     ''' test login invalid username and password '''
    #     self.common.driver.refresh()  # Fully reloads the login page
    #     time.sleep(2)
    #     self.logger.info("Step: Attempt login with invalid credential")
    #     fill_username_password(self.common,"user","pass")
    #     self.common.verify_text_contains(By.XPATH,LOGIN_PAGE_LOCATOR['toast'],ERROR['wrong_cred'])
    #     time.sleep(5)
    
    def test_004_login_valid_user(self):
        ''' test login valid user '''
        self.common.driver.refresh()  # Fully reloads the login page
        time.sleep(2)        
        self.logger.info("Step: Attempt login with valid credential")
        fill_username_password(self.common,USERNAME["std"],PASSWORD)
        time.sleep(5)

    def test_005_add_items(self):
        ''' test adding items from product page '''
        self.logger.info("Step: Attempt to add items to cart")
        add_items(self.common,"Backpack","Bike Light","Onesie")
        time.sleep(5)
    
    def test_006_remove_items(self):
        ''' Test removing items from product page , using same keyword as add to remove items '''
        self.logger.info("Step: Attempt to remove items from cart")
        add_items(self.common,"Bike Light")

    # def test_007_add_wrong_items(self):
    #     ''' Adding non existing items '''
    #     self.logger.info("Step: Attempt to add non existing items")
    #     is_exist = self.common.run_keyword_and_return_status(add_items,self.common,'Hello World')
    #     # self.common.run_keyword_and_ignore_error(add_items,self.common,'Hello World')
    #     self.logger.info(f"Can I add non exist items : {is_exist}")
        
    # def test_008_check_non_exist_items(self):
    #     ''' Checking for non existing items '''
    #     self.logger.info("Step: Attempt to check non existing items")
    #     check_non_exist_item(self.common,'Hello World')
    #     # self.common.run_keyword_and_return_status(check_non_exist_item,self.common,'Hello World')
    #     # self.common.run_keyword_and_ignore_error(check_non_exist_item,self.common,'Hello World')
        
    # def test_009_chance_sorting(self):
    #     ''' Change sorting methods '''
    #     sort_select = self.common.select_by_options(By.XPATH,PRODUCT_PAGE_LOCATOR['sort'],'index',2)
    #     self.logger.info(f"Sort selected : {sort_select}")
    #     time.sleep(5)
        
    #     sort_select = self.common.select_by_options(By.XPATH,PRODUCT_PAGE_LOCATOR['sort'],'value','za')
    #     self.logger.info(f"Sort selected : {sort_select}")
    #     time.sleep(5)
    
    def test_010_get_items_price(self):
        ''' Get item's price '''
        self.logger.info("Step : Attempt to get items price")
        print('Hello Hello My Friend.')
        get_items_price(self.common,"Backpack","Bike Light","Onesie")
        
    
    # def test_011_click_menu_burger(self):
    #     ''' Test menu burger. '''
    #     self.logger.info("Step : Attempt to click menu bar")
    #     select_menu(self.common,'about')
    #     time.sleep(5)
    #     self.driver.back()   # for about you need to go back to prev page.
        
    #     select_menu(self.common,'logout')
    #     self.common.wait_until_element_is_visible(By.XPATH,LOGIN_PAGE_LOCATOR['header'])
    #     time.sleep(5)
        
    def test_012_checking_item_in_cart(self):
        ''' Check the items that you added on test_005, 
        
        and don't forget to look which items you have been remove from test_006. '''
        self.logger.info("Step : Attempt to verify items in cart")
        self.common.wait_until_element_is_visible_then_click(By.XPATH,PRODUCT_PAGE_LOCATOR['cart'])
        check_items(self.common,"Backpack","Onesie")

if __name__ == '__main__':
    unittest.main()