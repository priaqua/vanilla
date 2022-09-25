from CBH.SRC.PageObject.Locators.Home import *
from CBH.SRC.TestBase import *
from CBH.SRC.PageObject.Pages.Sam_About_Item import get_txt_about
from CBH.SRC.PageObject.Locators.Sam_About_Item import *


def chk_about_txt(self,driver):
    get_txt_about(self,driver)

    if Locator.about_item_txt == "About this item":
        print("Pass- found About this item text on item Samsung TV")
    else:
        print("Test Fail About this item text not found")