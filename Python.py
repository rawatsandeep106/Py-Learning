from selenium import webdriver

driver = webdriver.Chrome('C:\\Users\\rawatsan\\Desktop\\My Python Projects\\chromedriver')
driver.get('https://www.google.com/')
driver.find_element_by_id('gb_70').click()

