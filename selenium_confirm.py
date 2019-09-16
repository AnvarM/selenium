from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_class_name("btn")
    button.click()
    
    confirm = browser.switch_to.alert
    confirm.accept()
    
    xElement = browser.find_element_by_id("input_value")
    x = xElement.text
    y = str(math.log(abs(12*math.sin(int(x)))))
    answerField = browser.find_element_by_id("answer")
    answerField.send_keys(y)
    submit = browser.find_element_by_class_name("btn")
    submit.click()
        
finally:
    time.sleep(30)
    browser.quit()