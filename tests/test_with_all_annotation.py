import allure
from allure_commons.types import Severity
from selene import browser, by, have, be


def test_dynamic_labels():
    allure.dynamic.tag("WEB")
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.feature("Задача в репозитории")
    allure.dynamic.story("Проверка наличия номера в Issues")
    allure.dynamic.link("https://github.com", name="Testing")
    browser.open("/")
    browser.element('[data-target="qbsearch-input.inputButton"]').click()
    browser.element('#query-builder-test').send_keys("AleksShakhmatov/PY_HW9_PageObject").press_enter()
    browser.element(by.link_text("AleksShakhmatov/PY_HW9_PageObject")).click()
    browser.element("#issues-tab").click()
    browser.all('.opened-by').element_by(have.text('#2')).should(be.visible)


@allure.tag("web")
@allure.severity(Severity.MINOR)
@allure.label("owner", "AleksSh")
@allure.feature("Задача в репозитории")
@allure.story("Проверка наличия номера в Issues")
@allure.link("https://github.com", name="Testing")
def test_decorator_labels():
    browser.open("/")
    browser.element('[data-target="qbsearch-input.inputButton"]').click()
    browser.element('#query-builder-test').send_keys("AleksShakhmatov/PY_HW9_PageObject").press_enter()
    browser.element(by.link_text("AleksShakhmatov/PY_HW9_PageObject")).click()
    browser.element("#issues-tab").click()
    browser.all('.opened-by').element_by(have.text('#2')).should(be.visible)
