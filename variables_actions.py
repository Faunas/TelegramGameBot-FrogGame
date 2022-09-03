def end_job():
    browser.find_element_by_css_selector('#column-center > div > div > div.chat-input > div > div.rows-wrapper-wrapper > div > div.new-message-wrapper > div.input-message-container > div.input-message-input.scrollable.scrollable-y.i18n.no-scrollbar').send_keys('@toadbot Завершить работу')
    browser.find_element_by_css_selector('#column-center > div.chats-container.tabs-container > div > div.chat-input > div > div.btn-send-container > button').click()
def eatmyfrog():
    browser.find_element_by_css_selector('#column-center > div > div > div.chat-input > div > div.rows-wrapper-wrapper > div > div.new-message-wrapper > div.input-message-container > div.input-message-input.scrollable.scrollable-y.i18n.no-scrollbar').send_keys('@toadbot Покормить жабу')
    browser.find_element_by_css_selector('#column-center > div.chats-container.tabs-container > div > div.chat-input > div > div.btn-send-container > button').click()
def kissfrog():
    browser.find_element_by_css_selector('#column-center > div > div > div.chat-input > div > div.rows-wrapper-wrapper > div > div.new-message-wrapper > div.input-message-container > div.input-message-input.scrollable.scrollable-y.i18n.no-scrollbar').send_keys('@toadbot Поцеловать The Sun')
    browser.find_element_by_css_selector('#column-center > div.chats-container.tabs-container > div > div.chat-input > div > div.btn-send-container > button').click()
def gotodetsad_smallfrog(): # Работает в промежутке с 6:00 до 12:00 по МСК.
    browser.find_element_by_css_selector('#column-center > div > div > div.chat-input > div > div.rows-wrapper-wrapper > div > div.new-message-wrapper > div.input-message-container > div.input-message-input.scrollable.scrollable-y.i18n.no-scrollbar').send_keys('@toadbot Отправить жабенка в детсад')
    browser.find_element_by_css_selector('#column-center > div.chats-container.tabs-container > div > div.chat-input > div > div.btn-send-container > button').click()
def takedetsad_smallfrog(): # Работает через 6 и до 8 часов после отправки жабенка в детсад.
    browser.find_element_by_css_selector('#column-center > div > div > div.chat-input > div > div.rows-wrapper-wrapper > div > div.new-message-wrapper > div.input-message-container > div.input-message-input.scrollable.scrollable-y.i18n.no-scrollbar').send_keys('@toadbot Забрать жабенка')
    browser.find_element_by_css_selector('#column-center > div.chats-container.tabs-container > div > div.chat-input > div > div.btn-send-container > button').click()
def gotojob_kitchen(): #
    browser.find_element_by_css_selector('#column-center > div > div > div.chat-input > div > div.rows-wrapper-wrapper > div > div.new-message-wrapper > div.input-message-container > div.input-message-input.scrollable.scrollable-y.i18n.no-scrollbar').send_keys('@toadbot Поход в столовую')
    browser.find_element_by_css_selector('#column-center > div.chats-container.tabs-container > div > div.chat-input > div > div.btn-send-container > button').click()