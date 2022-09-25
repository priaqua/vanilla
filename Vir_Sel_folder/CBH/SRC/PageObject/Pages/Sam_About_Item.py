from selenium.webdriver.common.by import By
from CBH.SRC.PageObject.Locators.Sam_About_Item import *



def get_txt_about(self,driver):
    driver.find_element(By.XPATH,Locator.about_item_txt)