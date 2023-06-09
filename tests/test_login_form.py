import time
from pages.form_page import FormPage
from selenium.webdriver.common.keys import Keys

def test_login_form(browser):
    form_page = FormPage(browser)

    form_page.visit()
    assert not form_page.modal_dialog.exist()
    time.sleep(2)
    form_page.first_name.send_keys('tester')
    form_page.last_name.send_keys('testerovich')
    form_page.user_email.send_keys('test@ttt.tt')
    form_page.gender_radio_1.click_force()
    form_page.user_number.send_keys('9992223344')
    form_page.hobbies.click_force()
    form_page.current_address.send_keys('546738jfh')

    form_page.city.scroll_to_element()
    #time.sleep(2)
    form_page.city.click()
    form_page.state_and_city.click()
    #form_page.state_and_city.send_keys('NCR')
    #form_page.state_and_city.send_keys(Keys.ENTER)
    time.sleep(2)
    form_page.btn_submit.click_force()
    time.sleep(2)

    assert form_page.modal_dialog.exist()
    form_page.btn_close_modal.click_force()




def test_state_and_city(browser):
    form_page = FormPage(browser)

    form_page.visit()
   #form_page.state.scroll_to_element()
    form_page.state.click()
    #form_page.state.send_keys(Keys.PAGE_DOWN)
    #form_page.state_and.send_keys('NCR')
    form_page.state_and.send_keys(Keys.ENTER)
    form_page.city.click()
    form_page.city_and.send_keys(Keys.ENTER)

