from CBH.SRC.PageObject.Locators.Home import *
from CBH.SRC.TestBase import *



if Locator.about_item_txt == "About this item":
    print("Pass- found About this item text on item Samsung TV")
else:
    print("Test Fail About this item text not found")