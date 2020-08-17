from selenium import webdriver
import time

input_data = input('What do you want to search :- ')

PATH = "C:\Program Files\chromedriver.exe"

driver = webdriver.Chrome(PATH)
driver.get('http://google.com')

main = driver.find_element_by_name('q')
main.send_keys(input_data)
main.submit()

time.sleep(5)

main = driver.find_element_by_class_name('r')
main.click()

time.sleep(5)

driver.quit()