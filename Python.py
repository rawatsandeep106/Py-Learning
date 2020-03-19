from selenium import webdriver

path = 'C:\\Users\\rawatsan\\Desktop\\My Python Projects\\ChromeDriver\\chromedriver.exe'
driver = webdriver.Chrome(path)

driver.maximize_window()
driver.delete_all_cookies()

driver = webdriver.Chrome(path)
driver.get('https://github.com/')
driver.find_element_by_xpath('/html/body/div[1]/header/div/div[2]/div[2]/a[1]').click()
driver.find_element_by_id('login_field').send_keys('rawatsandeep106')
driver.find_element_by_id('password').send_keys('Tarzan@864')
driver.find_element_by_xpath('//*[@id="login"]/form/div[4]/input[9]').click()
driver.find_element_by_xpath('/html/body/div[1]/header/div[6]/details/summary').click()
driver.get('https://github.com/new')

