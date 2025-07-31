from selenium.webdriver.common.by import By

LOGIN_PAGE_LOCATOR= {
    "username":"//input[@id='user-name']",
    "password":"//input[@id='password']",
    "header":"//div[contains(text(),'Swag Labs')]",
    "submit_btn":"//input[@id='login-button']",
    "toast":"//h3[@data-test='error']"
}

USERNAME={
    "std":"standard_user",
    "lck":"locked_out_user",
    "pbm":"problem_user",
    "pef":"performance_glitch_user",
    "err":"error_user",
    "ve":"visual_user"
}

PASSWORD="secret_sauce"

ERROR = {
    "wrong_cred":"Username and password do not match",
    "user_req":"Username is required",
    "pass_req":"Password is required",
}

def open_browser_with_url(driver,url):
    ''' Open Chrome as default browser with URL as parameter.'''
    driver.get(url)
    
def fill_username_password(common,username,password):
    common.fill_text(By.XPATH,LOGIN_PAGE_LOCATOR["username"],username)
    common.fill_text(By.XPATH,LOGIN_PAGE_LOCATOR["password"],password)
    common.wait_until_element_is_visible_then_click(By.XPATH,LOGIN_PAGE_LOCATOR["submit_btn"])