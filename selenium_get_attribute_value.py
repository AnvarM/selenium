from selenium import webdriver
import time
import math 

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    xElement = browser.find_element_by_id("treasure")
    x = int(xElement.get_attribute("valuex"))
    y = str(math.log(abs(12*math.sin(int(x)))))
    answerField = browser.find_element_by_id("answer")
    answerField.send_keys(y)
    isRobot = browser.find_element_by_id("robotCheckbox")
    isRobot.click()
    rule = browser.find_element_by_id("robotsRule")
    rule.click()
    submit = browser.find_element_by_class_name("btn")
    submit.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()