from selenium import webdriver
import time

def registration_form_check(link):
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
    
    browser.quit()
    return welcome_text