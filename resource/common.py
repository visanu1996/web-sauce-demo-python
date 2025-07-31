from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException


import os
import yaml
from datetime import datetime

from utils.logger import get_logger
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException


# report_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','reports')


class Common:
    def __init__(self,driver):
        self.driver = driver
        self.logger = get_logger(__name__)
    
    def read_yml(self,file_path):
        ''' Use to read yml file only. '''
        with open(file_path,'r') as file:
            return yaml.safe_load(file)
        
    def element_should_not_be_visible(self,by,locator,timeout=10):
        ''' To check that the element is not visible '''
        try:
            WebDriverWait(self.driver,timeout).until_not(
                EC.visibility_of_element_located((by,locator))
            )
            self.logger.info('Element is no longer exist.')
            
        except  Exception as e :
            self.logger.error(e)
            raise e
    
    def wait_until_element_is_visible(self,by,locator,timeout=10):
        ''' Wait for element to be visible '''
        try:
            element = WebDriverWait(self.driver,timeout).until(
                EC.visibility_of_element_located((by,locator))
            )
            self.logger.info(f"Element {locator} is visible.")
            return element
        except  TimeoutException as e:
            self.logger.error('Element is not visible.')
            raise e
        
    def wait_until_element_is_presence(self,by,locator,timeout=10):
        ''' Wait for element to be presence on the page, no need to be visible '''
        try:
            element = WebDriverWait(self.driver,timeout).until(
                EC.presence_of_element_located((by,locator))
            )
            self.logger.info(f"Element {locator} is presence.")
            return element
        except TimeoutException as e:
            self.logger.error('Element is not presence.')
            raise e
    
    def wait_until_element_is_visible_then_click(self,by,locator,timeout=10):
        ''' wait for the element to be visible then click it '''
        try:
            element = WebDriverWait(self.driver,timeout).until(
                EC.visibility_of_element_located((by,locator))
            )
            element.click()
            self.logger.info(f"Click element {locator}")
            return True

        except TimeoutException as e: 
            self.logger.error("Can't click element because element is not visible.")
            raise e
        
    def get_element_text(self, by, locator, timeout=10):
        try:
            element = WebDriverWait(self.driver,timeout).until(
                EC.visibility_of_element_located((by,locator))
            )
            self.logger.info(f"return element text : {element.text}")
            return element.text
        except TimeoutException as e:
            self.logger.error("Can't get element text because element is not visible.")
            raise e
        
    def get_element_rect_bound(self, by, locator, timeout=10):
        try:
            element = WebDriverWait(self.driver,timeout).until(
                EC.visibility_of_element_located((by,locator))
            )
            self.logger.info(f"return element rect : {element.rect}")
            return element.rect
        except TimeoutException as e:
            self.logger.error("Can't get element rect because element is not visible")
            raise e
        
    def run_keyword_and_return_status(self, func, *args, **kwargs):
        self.logger.info(f"Running function: {func.__name__} and returning status.")
        try:
            func(*args, **kwargs)
            self.logger.info("Function {func.__name__} Return: True")
            return True
        except Exception as e:
            self.logger.info("Function {func.__name__} Return: False")
            return False
        
    def run_keyword_and_ignore_error(self, func, *args, **kwargs):
        try:
            func(*args, **kwargs)
            # self.logger.info(f"Function {func.__name__} ran successfully (errors ignored).")
        except Exception as e:
            self.logger.warning(f"Ignored error in {func.__name__}")


    def fill_text(self, by, locator, text,timeout=10):
        try:
            element = WebDriverWait(self.driver,timeout).until(
                EC.visibility_of_element_located((by,locator))
            )
            element.clear()
            send_text = text if text != None else ""
            element.send_keys(send_text)
            self.logger.info(f"fill {locator} with text.")
        
        except  Exception as e:
            self.logger.error(f"error occure while send_keys : {e}")
            raise e
        except  TimeoutException:
            self.logger.error("Locator is not visible can't fill text.")
            raise e
        
    def verify_text_contains(self, by, locator, text, timeout=10):
        ''' verify text in string raise error if failed '''
        element_text = self.get_element_text(by,locator,timeout)
        if text in element_text:
            self.logger.info(f"Element text contains {text}.")
            return True
        else: 
            self.logger.error(f"Element text is not contains {text}.")
            raise f'Element text is not contains {text}.'
        
    def select_by_options(self,by ,locator,option,choice,timeout=10):
        ''' Select from a <select> tag by index,value or label (visible text).
            Return the selected option's text.
        
            Parameters:
            option - 'index', 'value' or 'label'
            choice - the value or index to select.
        '''
        
        try:
            element = self.wait_until_element_is_visible(by,locator,timeout)
            select = Select(element)
            
            if option.lower() == 'index':
                select.select_by_index(int(choice))
                
            elif option.lower() == 'value':
                select.select_by_value(choice)
                
            elif option.lower() == 'label':
                select.select_by_visible_text(choice)
            
            else:
                self.logger.error('Wrong option select')
                raise ValueError(f"Invalid selection option: {option}")
            
            element = self.wait_until_element_is_visible(by,locator,timeout)
            select = Select(element)
            selected_text = select.first_selected_option.text
            return selected_text
            
        except Exception as e :
            self.logger.error(f"Failed to select option '{choice}' by '{option}': {e}")
            raise e