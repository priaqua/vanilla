import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import pdb



driver=webdriver.Chrome()
driver.get('https://www.amazon.in')

#Click on Menu
ham=driver.find_element(By.CSS_SELECTOR,'#nav-hamburger-menu' )
ham.click()
driver.find_element(By.ID, 'hmenu-content')



# Under TV, Appliances, Electronics > Television

#click on Televisions under Tv, Audio & Cameras sub section.

#Not able to locate....either element is wrong or could be focus has to change to menu before clicking

#scroll to an item on the menu....Unable to locate element: {"method":"xpath","selector":"div[@id="hmenu-canvas"]"}
# canvas=driver.find_element(By.XPATH, 'div[@id="hmenu-canvas"]')
# driver.find_element(By.XPATH, 'a[(@class="hmenu-item" and text()="TV, Appliances, Electronics")]')
#driver.switch_to

#To move on for now using url to go to Television
driver.get('https://www.amazon.in/gp/browse.html?node=1389396031&ref_=nav_em_sbc_tvelec_television_0_2_9_2')

#scroll and go to Brands-Samsung- select checkbox Samsung

#driver.find_element(By.XPATH,"//div([@class="a-checkbox"]>[text()="Samsung"]")

#//div[@class="a-checkbox"]>/span[text()="Samsung"])')


# # Workaround to scroll -go to url Selected Samsung so that we move on.....fix and remove
driver.get('https://www.amazon.in/s?bbn=1389396031&rh=n%3A1389396031%2Cp_89%3ASamsung&dc&qid=1663245557&rnid=3837712031&ref=lp_1389396031_nr_p_89_4')
driver.maximize_window()
window_before = driver.window_handles[0]

#Select Sort By Dropdown
time.sleep(5)
sort_dropdown=driver.find_element(By.CLASS_NAME, 'a-dropdown-label')
#'a-button-dropdown')
time.sleep(3)
sort_dropdown.click()

#select High to Low
# Xpath H_L=driver.find_element(By.XPATH,'//*[@id="search"]/div[1]/div[1]/div/span[3]/div[2]/div[3]')
H_L=driver.find_element(By.ID, 's-result-sort-select_2')
#Xpath  '//*[@id="s-result-sort-select_2"]')
time.sleep(3)
H_L.click()

#To New Window
Second_H=driver.find_element(By.XPATH, '//*[@id="search"]/div[1]/div[1]/div/span[3]/div[2]/div[3]/div/div/div/div')
Second_H.click()
window_after = driver.window_handles[1]
#Switch to Second_H window
driver.switch_to.window(window_after)

Item=driver.find_element(By.XPATH,'//*[@id="feature-bullets"]/h1')
assert (Item.text=="About this item"),"About this item - is expected"
pdb.set_trace()

# def invokebrowser_opensite():
#     driver = webdriver.Chrome()
#     driver.get("https://www.google.com/")
#
#
# invokebrowser_opensite()
