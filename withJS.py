from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(chrome_options=options)

driver.get('file://example.html')

#p_element = driver.find_element_by_id('intro-text')
#print(p_element.text)
# result:
#'Yay! Supports javascript'