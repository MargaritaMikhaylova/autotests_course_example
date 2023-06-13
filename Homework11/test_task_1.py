# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста


from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


sbis_site = 'https://sbis.ru/'
driver = webdriver.Chrome()

def test_about():
    try:
        driver.get(sbis_site)
        sleep(3)
        assert driver.current_url == sbis_site, 'Неверный адрес сайта'
        contacts = driver.find_element(By.CSS_SELECTOR, '[href = "/contacts"]')
        contacts.click()
        sleep(3)
        banner = driver.find_element(By.CSS_SELECTOR, '.pb-16 [title = "tensor.ru"]')
        banner.click()
        sleep(1)
        driver.switch_to.window(driver.window_handles[1])
        sleep(3)
        force = driver.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__block4-content .tensor_ru-Index__card-title')
        assert force.is_displayed(), 'Блок "Сила в людях" не отображается'
        details = driver.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__block4-content [href="/about"]')
        details.location_once_scrolled_into_view
        assert details.is_displayed(), 'Кнопка "Подробнее" не отображается'
        details.click()
        sleep(3)
        about = 'https://tensor.ru/about'
        assert driver.current_url == about, 'Неверный адрес сайта'

    finally:
        sleep(2)
        driver.quit()
