from pages.webtables_team import WebtablesTeam
import time

def test_webtables(browser):
    webtables_team = WebtablesTeam(browser)

    webtables_team.visit()
    assert not webtables_team.no_rows_found.exist()

    while webtables_team.delete.exist():
        webtables_team.delete.click()

    time.sleep(2)

    assert webtables_team.no_rows_found.exist()
