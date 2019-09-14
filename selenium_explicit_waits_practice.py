from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
    
    bookButton = browser.find_element_by_id("book")
    bookButton.click()
  
    xElement = browser.find_element_by_id("input_value")
    x = xElement.text
    y = str(math.log(abs(12*math.sin(int(x)))))
    answerField = browser.find_element_by_id("answer")
    answerField.send_keys(y)
    submit = browser.find_element_by_id("solve")
    submit.click()
        
finally:
    time.sleep(30)
    # закрываем браузер
    browser.quit()