from selene import browser, by, have, be


def test_github():
    browser.open("/")

    browser.element('[data-target="qbsearch-input.inputButton"]').click()
    browser.element('#query-builder-test').send_keys("AleksShakhmatov/PY_HW9_PageObject").press_enter()

    browser.element(by.link_text("AleksShakhmatov/PY_HW9_PageObject")).click()

    browser.element("#issues-tab").click()

    browser.all('.opened-by').element_by(have.text('#2')).should(be.visible)
