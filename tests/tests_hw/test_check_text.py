from pages.demoqa import Demoqa
from pages.elements_page import ElementsPage


def test_check_text(browser):
    demo_qa_hw = Demoqa(browser)
    demo_qa_hw.visit()
    if demo_qa_hw.pod.get_text() == '© 2013-2020 TOOLSQA.COM|ALL RIGHTS RESERVED.':
        return True
    else:
        return False



def test_btn_text(browser):
    demo_qa_hw3 = Demoqa(browser)
    demo_qa_hw4 = ElementsPage(browser)
    demo_qa_hw3.visit()
    demo_qa_hw3.btn_hw.click()
    if demo_qa_hw4.prov.get_text() == 'Please select an item from left to start practice.':
        return True
    else:
        return False
def test_page_elements(browser):

    elements_page = ElementsPage(browser)

    elements_page.visit()
    assert elements_page.text_elements.get_text() == 'Elements'
    assert elements_page.icon_elements.exist()
    assert elements_page.btn_sidebar_first.exist()
    assert elements_page.btn_sidebar_first_textbox.exist()
