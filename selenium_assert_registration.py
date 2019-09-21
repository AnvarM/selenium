from selenium import webdriver
import time

try: 
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    firstNameElement = browser.find_element_by_css_selector('.first_block .first')
    firstNameElement.send_keys("UsrNm")
    lastNameElement = browser.find_element_by_css_selector('.first_block .second')
    lastNameElement.send_keys("UsrLstNm")
    emailElement = browser.find_element_by_css_selector('.first_block .third')
    emailElement.send_keys("nm.lstnm@ts.tst")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    
    time.sleep(2)
    
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()