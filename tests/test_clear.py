import time
from pages.text_box import TextBox

def test_clear(browser):
    textbox_page = TextBox(browser)
    textbox_page.visit()

    textbox_page.full.send_keys('yes')
    time.sleep(2)
    textbox_page.full.clear()
    time.sleep(2)
    assert textbox_page.full.get_text() == ''




