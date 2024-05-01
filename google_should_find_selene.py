from selene import browser, be, have

def test_google_find_selene():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))

def test_google_do_not_find():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.no.text('Coffe'))

def test_yandex_find_selene():
    browser.open('https://ya.ru')
    browser.element('#text').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('#search-result').should(have.text('yashaka/selene: User-oriented Web UI browser...'))

def test_yandex_do_not_find_coffe():
    browser.open('https://ya.ru')
    browser.element('#text').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('#search-result').should(have.no.text('Coffe'))