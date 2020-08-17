from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:\Program Files\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("https://www.google.com")

search = driver.find_element_by_name("q")
search.send_keys("test")
search.send_keys(Keys.ENTER)
print(driver.title)

# print(driver.page_source)   # to get the full source code of the website


try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "rso"))
    )
    print(main.text)
except:
    driver.quit()

# print(main.text)

# time.sleep(5)

# driver.close() # to close the particular tab
# driver.title # give the title of the web page
driver.quit() # to quit the web brower