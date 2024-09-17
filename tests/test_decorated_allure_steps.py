import allure
from selene import browser, by, have, be


def test_github_decorated_allure_steps():
    open_main_page()
    search_for_repository('AleksShakhmatov/PY_HW9_PageObject')
    go_to_repository('AleksShakhmatov/PY_HW9_PageObject')
    open_issue_tab()
    check_issue_number('2')


@allure.step("Открытие главной страницы")
def open_main_page():
    browser.open('/')


@allure.step("Поиск репозитория {repo}")
def search_for_repository(repo):
    browser.element('[data-target="qbsearch-input.inputButton"]').click()
    browser.element('#query-builder-test').send_keys(repo).press_enter()


@allure.step("Переход в репозиторий {repo}")
def go_to_repository(repo):
    browser.element(by.link_text(repo)).click()


@allure.step("Открытие вкладки Issues")
def open_issue_tab():
    browser.element('#issues-tab').click()


@allure.step("Проверка наличия в Issues номера #{number}")
def check_issue_number(number):
    browser.all('.opened-by').element_by(have.text(f'#{number}')).should(be.visible)
