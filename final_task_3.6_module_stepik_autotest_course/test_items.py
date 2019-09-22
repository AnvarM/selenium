link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_page_contains_add_to_basket_button(browser):
    browser.get(link)
    assert browser.find_element_by_css_selector(".btn-add-to-basket"), "On page should be button with class '.btn-add-to-basket'"
    
    