from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Remote(
    command_executor='https://www.example.in',
    options=chrome_options
)
driver.get("https://www.amazon.in")
