from CBH.SRC.PageObject.Pages.Television import locate_brand,samsung_chbox,clk_drpdown,sort_hi_lo,sec_hi_tv
from selenium.webdriver.common.by import By


def brand_selection(self, driver):
    locate_brand(self,driver)
    samsung_chbox(self, driver)
    assert driver.find_element(By.XPATH,'//*[contains(@id,"LG")]'), "LG is not selected"
    clk_drpdown(self, driver)
    sort_hi_lo(self, driver)
    sec_hi_tv(self, driver)


