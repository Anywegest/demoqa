import time

from pages.test_btn import TestBtn
from pages.test_koup import TestKoup

def test_btn_add(browser):
    test_btn = TestBtn(browser)
    test_koup = TestKoup(browser)
    test_btn.visit()

    assert test_btn.add_remove.get_text() == 'Add/Remove Elements'
    #assert test_btn.add_remove.exist() # можно и через exist

    test_btn.add_remove.click()
    assert test_koup.equal_url()

    assert test_koup.btn_add_element.get_text() == 'Add Element'
    #assert test_koup.add_element.exist()

    assert test_koup.btn_add_element.get_dom_attribute('onclick') == 'addElement()'

    for i in range(4):
        test_koup.btn_add_element.click()

    assert test_koup.btns_delete.check_count_elements(4)

    for element in test_koup.btns_delete.find_elements():
        assert element.text == 'Delete'

    while test_koup.btns_delete.exist():
        test_koup.btns_delete.click()
    assert not test_koup.btns_delete.exist()
    time.sleep(2)
