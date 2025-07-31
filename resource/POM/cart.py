from selenium.webdriver.common.by import By

CART_PAGE_LOCATOR = {
    "cart":"//a[@class='shopping_cart_link']",
    "header":"//span[@class='title']",
    "back_to_shopping":"//button[@id='continue-shopping']",
    "checkout":"//button[@id='checkout']"
}

ITEM_CARD = {
    "box":"//div[@class='cart_item' and ./div[@class='cart_item_label']/a/div[@class='inventory_item_name'  and contains(text(),'[[TO_CHANGE]]')]]",
    "qty":"//div[@class='cart_quantity']",
    "name":"//a/div[@class='inventory_item_name']",
    "desc":"//div[@class='inventory_item_desc']",
    "price":"//div[@class='inventory_item_price']",
    "add_remove":"//div[@class='item_pricebar']/button"
}


def check_items(common,*items):
    common.logger.info(f"Checking items in cart : {items}")
    for item in items:
        common.logger.info(f"currently item : {item}")
        item_box = ITEM_CARD['box'].replace('[[TO_CHANGE]]',item)
        common.verify_text_contains(By.XPATH,item_box+ITEM_CARD['name'],item)