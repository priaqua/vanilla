
### All the locators used in TELEVISION page
#locators in here are a Xpath, Class and ID

#brand                   :Xpath
# sam_checkbox           : Xpath
#sort_dropdown          : class
#'a-button-dropdown'
#High_Low               : id
#Second_Hi              :Xpath



class Locator(object):

    #Locator for navigation through Television page
    brand='//*[@id="s-refinements"]//div//span[(text()="Brands")]'
    sam_checkbox='//*[@id="s-refinements"]//div//span[contains (text(), "LG")]'
    sort_dropdown='a-dropdown-label'
    High_Low='s-result-sort-select_2'
    Second_Hi = '//*[@id="search"]/div[1]/div[1]/div/span[3]/div[2]/div[3]/div/div/div/div'
    #Locator to check Brand name check is as expected
    assert_brand='//*[contains(@id,"LG")]'

