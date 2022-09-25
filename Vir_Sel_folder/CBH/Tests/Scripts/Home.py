from selenium.webdriver.common.by import By
from CBH.SRC.PageObject.Pages.Home import menu_click, shop_by_cat, tv_appliance_electronics, television
from CBH.driver_config import *


# from CBH.driver_config import *

def home_page(driver):
    driver.get('https://www.amazon.in')
    driver.maximize_window()
    window_before = driver.window_handles[0]
    assert driver.find_element(By.CLASS_NAME, 'hm-icon-label'), "Cannot find Menu on Home Page"
def clickmenu(driver):
    menu_click(driver)
    shop_by_cat(driver)
    tv_appliance_electronics(driver)
    television(driver)
    assert driver.find_element(By.XPATH,
                               '//*[@id="nav-search-label-id"][text()="Televisions"]'), "Television page did not load"
