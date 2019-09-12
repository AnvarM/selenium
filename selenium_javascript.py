from selenium import webdriver
import time
browser = webdriver.Chrome()

browser.get(link)

browser.execute_script("alert('Robots at work');") # исполнит javascript код и выведет алерт с текстом 'Robots at work'

browser.execute_script("document.title='Script executing';") # изменит title текущей страницы на 'Script executing'
browser.execute_script('document.title="Script executing";')

button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button) # проскроллит страницу так, чтобы элемент button был в верхней части страницы
button.click()

browser.execute_script("window.scrollBy(0, 100);") # проскроллит страницу на 100 пикселей вниз

browser.quit()