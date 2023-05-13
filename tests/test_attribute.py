
from pages.text_box import TextBox
def test_placeholder(browser):
    textbox_page = TextBox(browser)

    textbox_page.visit()
    assert textbox_page.full.get_dom_attribute('placeholder') == 'Full Name'
