from pages.demoqa import Demoqa
def test_seo(browser):
    demo_qa_page = Demoqa(browser)

    demo_qa_page.visit()
    assert browser.title == demo_qa_page.pageData['title']
