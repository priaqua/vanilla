import time
import webbrowser

from selenium.webdriver.common.by import By
from CBH.SRC.PageObject.Locators.Home import Locator



def menu_click(self,driver):
    #time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, Locator.ham_menu)
    Locator.ham_menu.click()

def shop_by_cat(self,driver):
    driver.find_element(By.XPATH, Locator.element_shop_by_cat)
    driver.execute_script("arguments[0].scrollIntoView(true);",Locator.element_shop_by_cat)

# Locate scroll and click TV, Appliance, Electranics
def tv_appliance_electronics(self,driver):
    driver.find_element(By.XPATH, Locator.TV_App_Elect)
    driver.execute_script("arguments[0].scrollIntoView(true);", Locator.TV_App_Elect)
    #time.sleep(5)
    Locator.TV_App_Elect.click()

# Locate and click TV
def television(self,driver):
    driver.find_element(By.XPATH, Locator.TV)
    driver.execute_script("arguments[0].scrollIntoView(true);", Locator.TV)
    #time.sleep(5)
    Locator.TV.click()


