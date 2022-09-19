
import time
from selenium import webdriver
from selenium.webdriver.common.by import By



driver=webdriver.Chrome()
driver.get('https://www.amazon.in')
driver.maximize_window()
window_before = driver.window_handles[0]

###################
assert driver.find_element(By.CLASS_NAME, 'hm-icon-label'), "Cannot find Menu"
###################HOMEPAGE

#click menu
ham=driver.find_element(By.XPATH, '//*[@id="nav-hamburger-menu"]')
ham.click()

#Locate scroll and click TV, Appliance, Electranics
element_TAE= driver.find_element(By.XPATH, '//*[@id="hmenu-content"]/ul[1]/li[16]/a')
driver.execute_script("arguments[0].scrollIntoView(true);", element_TAE)
time.sleep(5)
element_TAE.click()

#Locate and click TV
element_TV= driver.find_element(By.XPATH, '//*[@id="hmenu-content"]/ul[9]/li[3]/a')
driver.execute_script("arguments[0].scrollIntoView(true);", element_TV)
time.sleep(5)
element_TV.click()

################TELEVISION
# Scroll to element Samsung and select checkbox(Change to better queries)
#Locate Brand
time.sleep(5)
element = driver.find_element(By.XPATH, '//*[@id="s-refinements"]/div[21]')
driver.execute_script("arguments[0].scrollIntoView(true);", element)
time.sleep(5)

#Select Samsung
#eventhough Xpath is pointing to Samsung click is on LG/Kodak intermittently-------Bug Fix it
sam_e=driver.find_element(By.XPATH,'//*[@id="s-refinements"]/div[21]/ul/li[6]/span/a/div/label/i')
sam_e.click()

#Select Sort By Dropdown
time.sleep(5)
sort_dropdown=driver.find_element(By.CLASS_NAME, 'a-dropdown-label')
time.sleep(3)
sort_dropdown.click()

#select High to Low
H_L=driver.find_element(By.ID, 's-result-sort-select_2')
time.sleep(3)
H_L.click()



#To New Window
Second_Hi=driver.find_element(By.XPATH, '//*[@id="search"]/div[1]/div[1]/div/span[3]/div[2]/div[3]/div/div/div/div')
Second_Hi.click()
window_after = driver.window_handles[1]

#Switch to Second_H window
driver.switch_to.window(window_after)

########Selected Samsung TV details page
Item=driver.find_element(By.XPATH,'//*[@id="feature-bullets"]/h1')
if Item.text=="About this item":
    print("Pass- found About this item text on item Samsung TV")
else:
    print("Test Fail About this item text not found")

driver.quit()