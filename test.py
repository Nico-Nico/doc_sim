from selenium import webdriver

options = webdriver.ChromeOptions()

options.add_argument('headless')

driver = webdriver.Chrome(chrome_options=options)

# Interacting with Facebook

