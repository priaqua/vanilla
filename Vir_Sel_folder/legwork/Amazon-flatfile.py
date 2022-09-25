
import time
from selenium import webdriver
from selenium.webdriver.common.by import By



driver=webdriver.Chrome()
driver.get('https://www.amazon.in')
driver.maximize_window()
window_before = driver.window_handles[0]
driver.implicitly_wait(5)

###################
assert driver.find_element(By.CLASS_NAME, 'hm-icon-label'), "Cannot find Menu on Home Page"
###################HOMEPAGE

#click menu
ham=driver.find_element(By.XPATH, '//*[@id="nav-hamburger-menu"]')
ham.click()
time.sleep(5)


#Locate scroll and click TV, Appliance, Electranics
#element_shop_by_dept=driver.find_element(By.XPATH, '//*[contains(@class,"hmenu-title")][text()="shop by department"]')
#Text on the site changed from "Shop by Department" to "Shop By Category"
element_shop_by_dept=driver.find_element(By.XPATH, '//*[contains(@class,"hmenu-title")][text()="shop by category"]')
driver.execute_script("arguments[0].scrollIntoView(true);", element_shop_by_dept)
element_TAE= driver.find_element(By.XPATH, '//*[@id="hmenu-content"]//a[@class="hmenu-item"]//div[contains(text(),"TV, Appliances, Electronics")]')
driver.execute_script("arguments[0].scrollIntoView(true);", element_TAE)
element_TAE.click()

#Locate and click TV
element_TV= driver.find_element(By.XPATH, '*//a[@class="hmenu-item"][contains(text(),"Televisions")]')
driver.execute_script("arguments[0].scrollIntoView(true);", element_TV)
element_TV.click()
assert driver.find_element(By.XPATH, '//*[@id="nav-search-label-id"][text()="Televisions"]'),"Television page did not load"

################TELEVISION
# Scroll to element Samsung and select checkbox(Change to better queries)
#Locate Brand
#element = driver.find_element(By.XPATH, '//*[@id="s-refinements"]/div[21]')
element_Brand = driver.find_element(By.XPATH, '//*[@id="s-refinements"]//div//span[(text()="Brands")]')
driver.execute_script("arguments[0].scrollIntoView(true);", element_Brand)

#Select Samsung
#commenting as Samsung is not available on Amazon
element_S=driver.find_element(By.XPATH,'//*[@id="s-refinements"]//div//span[contains (text(), "Samsung")]')
element_S.click()
assert driver.find_element(By.XPATH,'//*[contains(@id,"Samsung")]'), "Samsung is not selected"

#20th of September Samsung is not on Amazon site so to test changed the script to find LG....will revert back once Samsung is available
# element_LG=driver.find_element(By.XPATH, '//*[@id="s-refinements"]//div//span[contains (text(), "LG")]')
# element_LG.click()
# assert driver.find_element(By.XPATH,'//*[contains(@id,"LG")]'), "LG is not selected"


#Select Sort By Dropdown

sort_dropdown=driver.find_element(By.CLASS_NAME, 'a-dropdown-label')
sort_dropdown.click()
time.sleep(5)

#select High to Low
H_L=driver.find_element(By.ID, 's-result-sort-select_2')
H_L.click()



#To New Window
Second_Hi=driver.find_element(By.XPATH, '//*[@id="search"]/div[1]/div[1]/div/span[3]/div[2]/div[3]/div/div/div/div')
Second_Hi.click()
window_after = driver.window_handles[1]

#Switch to Second_H window
driver.switch_to.window(window_after)
element_brand_pg = driver.find_element(By.XPATH, '//*[contains(@class,"a-text-bold")][text()="Brand"]')
driver.execute_script("arguments[0].scrollIntoView(true);", element_brand_pg)
#20th of September Samsung is not on Amazon site so to test changed the script to find LG....will revert back once Samsung is available
#assert driver.find_element(By.XPATH, '//*[@class="a-size-base"][text()="LG"]'),"Expected Brand is not selected"
assert driver.find_element(By.XPATH, '//*[@class="a-size-base"][text()="Samsung"]'),"Expected Brand is not selected"



########Selected Samsung TV details page
Item=driver.find_element(By.XPATH,'//*[@id="feature-bullets"]/h1')
if Item.text=="About this item":
    print("Pass- found 'About this item' text on item Samsung TV")
else:
    print("Test Fail 'About this item' text not found")

driver.quit()