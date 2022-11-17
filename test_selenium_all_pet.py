import pytest
import time

from pytest_selenium import driver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# driver = webdriver.Chrome()
# driver.implicitly_wait(10)
# implicitly_waits = driver.find_elements("xpath", '//*[@id="all_my_pets"]/table/tbody')
#         # таблица на стр https://petfriends.skillfactory.ru/my_pets

@pytest.fixture(autouse=True)
def testing():
    pytest_driver = webdriver.Chrome()
    # pytest_driver = webdriver.Chrome('/patch/chromedriver')
    # Переходим на страницу авторизации
    pytest_driver.get('https://petfriends.skillfactory.ru/login')
    time.sleep(5)

    yield pytest_driver
    pytest_driver.quit()


# def click():
#     pass


def test_show_my_pets(testing):
    driver = testing
    # Вводим email
    driver.find_element('id', "email").send_keys('kaktusik99@mail.ru')
    time.sleep(3)
    # Вводим пароль
    driver.find_element('id', "pass").send_keys('Rkzrcf1976')
    time.sleep(3)
    # Нажимаем на кнопку входа в аккаунт
    driver.find_element("css selector", 'button[type="submit"]').click()
    time.sleep(3)
    # Проверяем, что мы оказались на главной странице пользователя
    assert driver.find_element("tag name", 'h1').text == "PetFriends"
    # Нажать кнопку "Мои питомцы"
    driver.find_element("xpath", '//*[contains(text(),"Мои питомцы")]').click()
    time.sleep(3)

    # # ###### "xpath", '//div[@class=".col-sm-4 left")]'
    # # Находим локатор на профиль статистики и извлекаем текст
    # all_my = driver.find_element('link text', u"Питомцев").get_attribute('innerText')
    # # Извлекаем текст до слова Друзей
    # find_pets = all_my[0:all_my.find('Друзей')]
    # # Извлекаем числа из find_pets
    # value = int("".join(filter(str.isdigit, find_pets)))
    # value2 = int(driver.find_element('link text', u"Питомцев").text.split()[2])
    #
    # print('\nall_my_pets_number ->', value, '||', value2)
    # driver.quit()


    # try:
    #     explicit_waits = WebDriverWait(driver, 10).until(
    #         EC.presence_of_element_located((By.XPATH, '//*[@id="all_my_pets"]')))
    #     assert explicit_waits == 'all_my_pets'
    #     print('Элемент найден')
    # except TimeoutException:
    #     print('What???')
    # finally:
    #     driver.quit()


    descriptions = driver.find_elements("xpath", '//*[@id="all_my_pets"]/table/tbody')
    images = driver.find_elements("xpath", '//*[id="all_my_pets"]//img')
    names = driver.find_elements("xpath", '//*[@id="all_my_pets"]//body/tr/td[0]')
    statistics = driver.find_elements("xpath", '//div[@class=".col-sm-4 left"]/text[1]')
    f = filter(str.isdecimal, statistics)
    statistics_2 = "".join(f)  # оставляем только число из текста

    for i in range(len(names)):
        assert statistics_2 == len(descriptions)  # Присутствуют все питомцы
        assert statistics_2 == len(images)  # Хотя бы у половины питомцев есть фото
        assert statistics_2 == len(names)  # У всех питомцев есть имя, возраст и порода


animals_names = ['Patrik', 'star']
unique = []


def test_get_unique_names():  # У всех питомцев разные имена
    for animals_names in unique:
        if animals_names in unique:
            continue
        else:
            unique.append(animals_names)
        return unique


print(test_get_unique_names())