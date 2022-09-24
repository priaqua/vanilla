### All the locators used in Home page
#locators in here are a Xpath, Class and ID

#menutext              :Class
# ham_menu             :CSS selector
# TV_App_Elect and TV  :Xpath

# Choose better queries
# TV= driver.find_element(By.PARTIAL_LINK_TEXT, 'television')
# //*[@id="hmenu-content"][@text()="Televisions"]

def assert_Homepg_load(self):
        # Locator for assertion -Home page loaded
        assert_menutext = 'hm-icon-label'

class Locator(object):


        # Locators for navigation on Home page
        ham_menu='#nav-hamburger-menu>span'
        TV_App_Elect='//*[@id="hmenu-content"]//a[@class="hmenu-item"]//div[contains(text(),"TV, Appliances, Electronics")]'
        TV='*//a[@class="hmenu-item"][contains(text(),"Televisions")]'
        #Locator for assertion -Television page loaded
        assert_TV_pg='//*[@id="nav-search-label-id"][text()="Televisions"]'