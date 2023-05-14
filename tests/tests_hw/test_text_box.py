from pages.text_box import TextBox



def test_text_box(browser):
    textbox_page = TextBox(browser)
    textbox_page.visit()
    textbox_page.full.send_keys('good')
    textbox_page.current_address.send_keys('How are you?')
    textbox_page.submit.click()
