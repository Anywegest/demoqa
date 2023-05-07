import time

from pages.accordian import Accordian

def test_visible_accordian(browser):
    accordian_page = Accordian(browser)

    accordian_page.visit()
    accordian_page.lem.click()
    time.sleep(3)
    assert not accordian_page.sec.visible()
    #assert accordian_page.sec.visible()


def test_visible_accordian_default(browser):
    accordian_page = Accordian(browser)

    accordian_page.visit()
    assert not accordian_page.tion.visible()
    assert not accordian_page.ment.visible()
    assert not accordian_page.mol.visible()
