import time
from selenium.webdriver.common.by import By
from CBH.SRC.PageObject.Locators.Home import Locator


def menu_click(self,driver):
    #time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, Locator.ham_menu)
    Locator.ham_menu.click()

# Locate scroll and click TV, Appliance, Electranics
def TV_Appliance_Electronics(self,driver):
    driver.find_element(By.XPATH, Locator.TV_App_Elect)
    driver.execute_script("arguments[0].scrollIntoView(true);", Locator.TV_App_Elect)
    #time.sleep(5)
    Locator.TV_App_Elect.click()

# Locate and click TV
def Television(self,driver):
    driver.find_element(By.XPATH, Locator.TV)
    driver.execute_script("arguments[0].scrollIntoView(true);", Locator.TV)
    #time.sleep(5)
    Locator.TV.click()


