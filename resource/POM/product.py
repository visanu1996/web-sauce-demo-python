from selenium.webdriver.common.by import By
import time


PRODUCT_PAGE_LOCATOR = {
    "header":"//span[@class='title']",
    "cart":"//a[@class='shopping_cart_link']",
    "sort":"//select[@class='product_sort_container']",
    "menu_burger":"//button[@id='react-burger-menu-btn']",
}

MENU_BURGER = "//a[text()='[[TO_CHANGE]]']"


ITEM_CARD = {
    "box":"//div[@class='inventory_item_description' and ./div[@class='inventory_item_label']/a/div[contains(text(),'[[ITEM_NAME]]')]]",
    "name":"//a/div[@class='inventory_item_name ']",
    "desc":"//div[@class='inventory_item_desc']",
    "price":"//div[@class='pricebar']/div",
    "add_remove":"//div[@class='pricebar']/button"
}

def add_items(common,*items):
    try:
        for item in items:
            
            item_box = ITEM_CARD['box'].replace('[[ITEM_NAME]]',item)
            item_name = common.get_element_text(By.XPATH,item_box + ITEM_CARD['name'])
            common.wait_until_element_is_visible_then_click(By.XPATH,item_box + ITEM_CARD['add_remove'])
            common.logger.info(f"Adding Item : {item_name}")
            time.sleep(2)
            
    except TimeoutError as e:
        raise e
    
def check_non_exist_item(common,*items):
    try:
        for item in items:
            
            item_box = ITEM_CARD['box'].replace('[[ITEM_NAME]]',item)
            common.element_should_not_be_visible(By.XPATH,item_box)
            time.sleep(2)
            
    except TimeoutError as e:
        raise e

def get_items_price(common,*items):
    ''' Getting items price and store in Dictionary.
    
        Return a dictionary of item and it price.
    '''
    
    try:
        item_prices = {}
         
        for item in items:
            
            item_box = ITEM_CARD['box'].replace('[[ITEM_NAME]]',item)
            item_name = common.get_element_text(By.XPATH,item_box + ITEM_CARD['name'])
            item_price = common.get_element_text(By.XPATH,item_box + ITEM_CARD['price'])
            
            item_prices[item_name] = {"price":item_price}
            
            time.sleep(2)
        
        
        common.logger.info(item_prices)
        
        # # # to access it # # #
        # for item_name, item_info in item_prices.items():
        #     common.logger.info(f"[{item_name}] : ")
        #     for key , value in item_info.items():  
        #         common.logger.info(f"{key} : {value}")
        
        return item_prices
    except TimeoutError as e:
        raise e

def select_menu(common,menu):
    ''' Choose menu from munu burger.
    
        For menu choose ['All Items','About','Logout','Reset App State']
        note. you can write menu with capital, lower or title as you choose.
    '''
    menu_title = menu.title()
    common.wait_until_element_is_visible_then_click(By.XPATH,PRODUCT_PAGE_LOCATOR['menu_burger'])
    to_click = MENU_BURGER.replace('[[TO_CHANGE]]',menu_title)
    common.wait_until_element_is_visible_then_click(By.XPATH,to_click)
    