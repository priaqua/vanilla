
from selenium.webdriver.common.by import By
from CBH.SRC.PageObject.Pages.Home import *
from CBH.SRC.TestBase.WebdriverSetup import *
from selenium import webdriver

# class Testcase:
#     def __init__(self):
#         driver=webdriver.Chrome()
#         Home_Page(self)
#         driver.find_elements(By.XPATH, Locator.ham_menu)

def Homepg(driver):
        driver.find_elements(By.XPATH, Locator.ham_menu)

if Locator.ham_menu == "All":
    print("Pass- found text of menu_title-All")
else:
    print("Test Fail- Could not find text of menu_title-All")






