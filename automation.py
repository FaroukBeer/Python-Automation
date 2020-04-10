from selenium import webdriver 

chrome_browser = webdriver.Chrome('./chromedriver')

chrome_browser.maximize_window()

chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

assert('Selenium Easy' in chrome_browser.title)

show_message_button = chrome_browser.find_element_by_class_name('btn-default')

# print(button_text.get_attribute('innerHTML'))

assert 'Show Message' in chrome_browser.page_source

user_message = chrome_browser.find_element_by_id('user-message')

user_message.clear()

user_message.send_keys('I\'m Julia')

show_message_button.click()

chrome_browser.close()