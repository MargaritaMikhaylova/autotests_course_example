# Перейти на  https://sbis.ru/
# В Footer'e найти "Скачать СБИС"
# Перейти по ней
# Скачать СБИС Плагин для вашей ОС в папку с данным тестом
# Убедиться, что плагин скачался
# Вывести на печать размер скачанного файла в мегабайтах
# Для сдачи задания пришлите код и запись с экрана прохождения теста


from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from pathlib import Path
import os

sbis_site = 'https://sbis.ru/'
driver = webdriver.Chrome()

try:
    driver.get(sbis_site)
    sleep(3)
    assert driver.current_url == sbis_site, 'Неверный адрес сайта'
    download = driver.find_element(By.CSS_SELECTOR, '[href="/download?tab=ereport&innerTab=ereport25"]')
    download.location_once_scrolled_into_view
    download.click()
    sleep(2)
    cookie = driver.find_element(By.CSS_SELECTOR, '.sbisru-CookieAgreement__close')
    cookie.click()
    plugin = driver.find_element(By.CSS_SELECTOR, '[data-id="plugin"] .controls-TabButton__caption')
    assert plugin.get_attribute('innerText') == 'СБИС Плагин', 'Неправильная вкладка'
    sleep(1)
    plugin_button = driver.find_element(By.CSS_SELECTOR, '[data-id="plugin"] .controls-tabButton__overlay')
    plugin_button.click()
    sleep(1)
    min_ver = driver.find_element(By.CSS_SELECTOR,
                                  '[href="https://update.sbis.ru/Sbis3Plugin/master/min/win32/sbis3plugin-setup-min.msi"]')
    # min_ver.location_once_scrolled_into_view
    sleep(1)
    min_ver.click()
    sleep(2)
    work_dir = Path.cwd()
    download_in = os.path.join(os.path.join(work_dir), 'sbis3plugin-setup-min.msi')
    sleep(2)
    file_size = os.path.getsize(download_in)
    print(file_size)
finally:
    sleep(2)
    driver.quit()
