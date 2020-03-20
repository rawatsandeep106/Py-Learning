import pyautogui
import pyperclip
from sys import argv
from selenium import webdriver


def RepositoryCreation(rep_name):
    path = 'C:\\Users\\rawatsan\\Desktop\\My Python Projects\\ChromeDriver\\chromedriver.exe'
    driver = webdriver.Chrome(path)
    driver.delete_all_cookies()

    driver.maximize_window()
    driver.get('https://github.com/login/')
    driver.find_element_by_id('login_field').send_keys('rawatsandeep106')
    driver.find_element_by_id('password').send_keys('Tarzan@864')
    driver.find_element_by_xpath('//*[@id="login"]/form/div[4]/input[9]').click()
    driver.get('https://github.com/new')
    driver.find_element_by_id('repository_name').send_keys(rep_name)
    driver.find_element_by_id('repository_auto_init').click()

    tick_appear = pyautogui.locateOnScreen('tick.png', 10)
    pyautogui.click(tick_appear)

    driver.find_element_by_xpath('//*[@id="new_repository"]/div[3]/button').click()
    driver.find_element_by_xpath('//*[@id="js-repo-pjax-container"]/div[2]/div/div[3]/span/details/summary').click()
    driver.implicitly_wait(3)
    driver.find_element_by_xpath('//*[@id="js-repo-pjax-container"]/div[2]/div/div[3]/span/details/div/div/div[1]/div[1]/div/div/clipboard-copy').click()
    rep_link = pyperclip.paste()
    return rep_link


print(RepositoryCreation(argv[1]))
