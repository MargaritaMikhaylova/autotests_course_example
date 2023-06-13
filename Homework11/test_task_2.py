# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста


from selenium import webdriver
from time import sleep
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By

fix_site = 'https://fix.sbis.ru/'
driver = webdriver.Chrome()


def test_message():
    try:
        driver.get(fix_site)
        sleep(3)
        assert driver.current_url == fix_site, 'Неверный адрес сайта'
        start_work = driver.find_element(By.CSS_SELECTOR, '.sbisru-Button--primary')
        assert start_work.text == 'Начать работу'
        assert start_work.is_displayed(), 'Элемент не отображается'
        start_work.click()
        driver.switch_to.window(driver.window_handles[1])
        sleep(4)
        login = driver.find_element(By.CSS_SELECTOR, '[name="Login"]')
        sleep(1)
        login.send_keys('Alfadir', Keys.ENTER)
        assert login.get_attribute('value') == 'Alfadir'
        sleep(1)
        password = driver.find_element(By.CSS_SELECTOR, '[name="Password"]')
        password.send_keys('Alfadir123', Keys.ENTER)
        sleep(5)
        contacts = driver.find_element(By.CSS_SELECTOR, '[name="item-contacts"] [data-qa="NavigationPanels-Accordion__icon"]')
        sleep(1)
        action_chains = ActionChains(driver)
        action_chains.move_to_element(contacts)
        sleep(2)
        action_chains.click(contacts)
        action_chains.perform()
        sleep(3)
        plus = driver.find_element(By.CSS_SELECTOR, '.controls-Button_filled .icon-RoundPlus')
        plus.click()
        sleep(3)
        search = driver.find_element(By.CSS_SELECTOR, '.controls-StackTemplate-content .controls-InputBase__nativeField_hideCustomPlaceholder')
        sleep(2)
        search.send_keys('Курочкин Вадим')
        sleep(2)
        recipient = driver.find_element(By.CSS_SELECTOR, '.person-BaseInfo')
        sleep(2)
        recipient.click()
        sleep(2)
        text_box = driver.find_element(By.CSS_SELECTOR, '[data-qa="textEditor_slate_Field"]')
        sleep(2)
        text_box.send_keys('Тестовое сообщение себе', Keys.LEFT_CONTROL + Keys.ENTER)
        sleep(2)
        first_mail = driver.find_element(By.CSS_SELECTOR,
                                         '.controls-MasterDetail_details .controls-ListView__item__marked_default .msg-dialogs-item__message-text > p')
        assert first_mail.get_attribute('innerText') == 'Тестовое сообщение себе', 'Искомое сообщение не найдено'
        action_chains.context_click(first_mail)
        action_chains.perform()
        delete = driver.find_element(By.CSS_SELECTOR, '.controls-Menu__popup-content [title="Перенести в удаленные"]')
        delete.click()
        sleep(1)
        first_mail = driver.find_element(By.CSS_SELECTOR,
                                         '.controls-MasterDetail_details .controls-ListView__item__marked_default .msg-dialogs-item__message-text > p')
        assert first_mail.get_attribute('innerText') != 'Тестовое сообщение себе', 'Сообщение не удалено'
    finally:
        sleep(2)
        first_mail = driver.find_element(By.CSS_SELECTOR,
                                         '.controls-MasterDetail_details .controls-ListView__item__marked_default .msg-dialogs-item__message-text > p')
        if first_mail.get_attribute('innerText') == 'Тестовое сообщение себе':
            action_chains.context_click(first_mail)
            action_chains.perform()
            delete = driver.find_element(By.CSS_SELECTOR,
                                         '.controls-Menu__popup-content [title="Перенести в удаленные"]')
            delete.click()
        driver.quit()
