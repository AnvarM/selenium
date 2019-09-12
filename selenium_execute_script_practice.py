from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = int(browser.find_element_by_id("input_value").text)
    y = str(math.log(abs(12*math.sin(int(x)))))
    
    browser.execute_script("window.scrollBy(0, 100);") # скроллим вниз
    
    answerElement = browser.find_element_by_id("answer")
    answerElement.send_keys(y)
    
    isRobot = browser.find_element_by_id("robotCheckbox")
    isRobot.click()
    
    rules = browser.find_element_by_id("robotsRule")
    rules.click()
    
    button = browser.find_element_by_class_name("btn")
    button.click()
    
finally:
    time.sleep(30)
    # закрываем браузер
    browser.quit()