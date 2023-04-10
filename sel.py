import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация ChromeDriver
driver = webdriver.Chrome()

# Раскрываем браузер на весь экран
driver.maximize_window()

driver.get('http://www.seventest.com')

# Ожидаем (до 10 сек) загрузки элемента на странице, чтобы продожить работу
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'mainmenu')))

# Осуществляем поиск кнопки "Форум" и кликаем на неё
forum_button = driver.find_element(By.XPATH, '//a[@title="Форум для зарегистрированных пользователей Seventest"]')
forum_button.click()

# Ожидаем загрузки страницы (до 5 сек)
driver.implicitly_wait(5)

# Осуществляем поиск элемента и создаем переменную куда помещаем текстовое значение элемента
text_forum = driver.find_element(By.XPATH, '//span[@class="gen"]')
value_text_forum = text_forum.text

# Проверяем, что текст "Форум сайта Seventest" содержится в переменной value_text_forum
assert "Форум сайта Seventest" in value_text_forum

# Или же можно проверить по ожидаемой и фактической URL
url = "http://forum.seventest.com/"
get_url = driver.current_url

assert get_url == url

# Если проверки assert пройдены, то выводим оповещение о пройденном тесте
print('Test №1 complete!')

# Делаем скриншот для подтверждения прохождения теста с указанием фактического времени в названии файла
actual_date = datetime.datetime.utcnow().strftime("%Y.%m.%d %H.%M.%S")
name_screenshot = 'test_1_complete_' + actual_date + '.png'
driver.save_screenshot('C:\\screenshots\\' + name_screenshot)

# Закрываем браузер
driver.close()
