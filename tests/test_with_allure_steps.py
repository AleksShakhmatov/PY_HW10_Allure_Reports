import allure
from selene import browser, by, have, be


def test_github_with_allure_steps():
    with allure.step("Открытие главной страницы"):
        browser.open("/")

    with allure.step("Поиск репозитория"):
        browser.element('[data-target="qbsearch-input.inputButton"]').click()
        browser.element('#query-builder-test').send_keys("AleksShakhmatov/PY_HW9_PageObject").press_enter()

    with allure.step("Переход в репозиторий"):
        browser.element(by.link_text("AleksShakhmatov/PY_HW9_PageObject")).click()

    with allure.step("Открытие вкладки Issues"):
        browser.element("#issues-tab").click()

    with allure.step("Проверка наличия в Issues номера #2!"):
        browser.all('.opened-by').element_by(have.text('#2')).should(be.visible)
