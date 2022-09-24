from time import time
from selenium.webdriver.common.by import By
from CBH.SRC.PageObject.Locators.Television import  *


# Scroll to element Samsung and select checkbox(Change to better queries)

# Locate Brand
class Television(object):
    def locate_brand(sellf,driver):
        time.sleep(5)
        driver.find_element(By.XPATH, Locator.brand)
        driver.execute_script("arguments[0].scrollIntoView(true);", Locator.brand)
        time.sleep(5)


    #Select Samsung
    #eventhough Xpath is pointing to Saamsung click is on LG
    def samsung_chbox(self,driver):
        driver.find_element(By.XPATH,Locator.sam_checkbox)
        Locator.sam_checkbox.click()


    #Select Sort By Dropdown
    def clk_drpdown(self,driver):
        time.sleep(5)
        driver.find_element(By.CLASS_NAME, Locator.sort_dropdown)
        time.sleep(3)
        Locator.sort_dropdown.click()

    # select High to Low
    def sort_hi_lo(self,driver):
        driver.find_element(By.ID, Locator.High_Low)
        time.sleep(3)
        Locator.High_Low.click()

    #To New Window
    def sec_hi_tv(self,driver):
        driver.find_element(By.XPATH, Locator.Second_Hi)
        Locator.Second_Hi.click()
        window_after = driver.window_handles[1]
        #Switch to Second_H window
        driver.switch_to.window(window_after)
