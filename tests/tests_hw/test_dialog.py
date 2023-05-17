import time
from selenium.webdriver.common.keys import Keys
from pages.webtables_team import WebtablesTeam

def test_dialog(browser):
    webtables_team = WebtablesTeam(browser)
    webtables_team.visit()

    assert webtables_team.add.get_text() == 'Add'
    webtables_team.add.click()

    webtables_team.first_name.send_keys('tester')
    webtables_team.last_name.send_keys('Alden')
    webtables_team.user_email.send_keys('mvcj@example.com')
    webtables_team.age.send_keys('20')
    webtables_team.salary.send_keys('5000')
    webtables_team.department.send_keys('scientific')
    webtables_team.btn_submit.click()
    time.sleep(3)
    webtables_team.pencil.click()
    time.sleep(2)
    webtables_team.first_name.clear()
    webtables_team.first_name.send_keys('Felix')
    webtables_team.btn_submit.click()
    time.sleep(5)





def test_next_previous(browser):
    webtables_team = WebtablesTeam(browser)
    webtables_team.visit()

    webtables_team.rown.click()
    webtables_team.rown_elem.click()

    webtables_team.rown.exist()


    webtables_team.add.click()
    webtables_team.first_name.send_keys('max')
    webtables_team.last_name.send_keys('al')
    webtables_team.user_email.send_keys('jhhv@example.com')
    webtables_team.age.send_keys('44')
    webtables_team.salary.send_keys('2300')
    webtables_team.department.send_keys('technical')
    webtables_team.btn_submit.click()

    webtables_team.add.click()
    webtables_team.first_name.send_keys('sten')
    webtables_team.last_name.send_keys('den')
    webtables_team.user_email.send_keys('kfjgk@example.com')
    webtables_team.age.send_keys('56')
    webtables_team.salary.send_keys('25000')
    webtables_team.department.send_keys('news')
    webtables_team.btn_submit.click()

    webtables_team.add.click()
    webtables_team.first_name.send_keys('skott')
    webtables_team.last_name.send_keys('son')
    webtables_team.user_email.send_keys('kghjfd@example.com')
    webtables_team.age.send_keys('22')
    webtables_team.salary.send_keys('3100')
    webtables_team.department.send_keys('marketing')
    webtables_team.btn_submit.click()
    time.sleep(3)
    webtables_team.next.click()
    time.sleep(3)
    webtables_team.previous.click()
    time.sleep(3)

