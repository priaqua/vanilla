### All the locators used in Selected Samsung TV page -the second highest pricesed TV
#locators in here is Xpath,

#about_item_txt :Xpath

class Locator(object):

    #assert correct Brand is selected
    check_brand_pg ='//*[contains(@class,"a-text-bold")][text()="Brand"]'
    assert_brand_name ='//*[@class="a-size-base"][text()="LG"]'
    #Testpass variable for if statement-check for 'About This Item'
    about_item_txt = '//*[@id="feature-bullets"]/h1'
