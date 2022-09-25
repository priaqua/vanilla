import self as self
import time
from CBH.Tests.Scripts.Home import *
from CBH.Tests.Scripts.Television import *
from CBH.Tests.Scripts.Sam_About_Item import *
from CBH.driver_config import *
from selenium import webdriver
from pytest_selenium import *


# File"C:\Users\pria\Vir_Sel_folder\CBH\Tests\Scripts\Home.py", line14, in Home_Page
# menu_click(driver)
# TypeError: menu_click()
# missing 1 required positional argument: 'driver'

# @pytest.fixture(scope="session")
# def test_amazon(driver):
#     home_page(driver)
#     clickmenu(driver)
#     brand_selection(self, driver)
#     chk_about_txt(self, driver)



def amazon(driver):
    home_page(driver)
    clickmenu(driver)
    brand_selection(self, driver)
    chk_about_txt(self, driver)