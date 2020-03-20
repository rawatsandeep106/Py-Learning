from selenium import webdriver
path = 'C:\\Users\\rawatsan\\Desktop\\My Python Projects\\ChromeDriver\\chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get('https://www.google.com/')
driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input').send_keys('Yahoo')
driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]').click()
