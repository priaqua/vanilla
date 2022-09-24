from selenium.webdriver.common.by import By
from CBH.SRC.PageObject.Pages.Home import menu_click, TV_Appliance_Electronics, Television

def Home_Page(self, driver):
    driver.get('https://www.amazon.in')
    driver.maximize_window()
    window_before = driver.window_handles[0]
    assert driver.find_element(By.CLASS_NAME, 'hm-icon-label'), "Cannot find Menu on Home Page"
#def clickmenu(driver):
    menu_click(self=driver)
    TV_Appliance_Electronics(driver)
    Television(driver)
    assert driver.find_element(By.XPATH,
                                   '//*[@id="nav-search-label-id"][text()="Televisions"]'), "Television page did not load"


