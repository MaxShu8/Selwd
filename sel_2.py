import datetime
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


# фоновый режим без отрисовки UI
chrome_options = Options()
chrome_options.add_argument('--headless')

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

driver.get('https://www.saucedemo.com')

login = driver.find_element(By.XPATH, '//input[@id="user-name"]')
login.send_keys('standard_user')

password = driver.find_element(By.XPATH, '//input[@id="password"]')
password.send_keys('secret_sauce')

login_button = driver.find_element(By.XPATH, '//input[@id="login-button"]')
login_button.click()

# choice a jacket
choice_j = driver.find_element(By.XPATH, '//a[@id="item_5_title_link"]')
choice_j.click()

name_clothes = driver.find_element(By.XPATH, '//div[@class="inventory_details_name large_size"]')
actual_name_clothes = name_clothes.text

find_price = driver.find_element(By.XPATH, '//div[@class="inventory_details_price"]')
actual_price = find_price.text

print(f'{actual_name_clothes} - {actual_price}')

move_to_cart = driver.find_element(By.XPATH, '//button[@class="btn btn_primary btn_small btn_inventory"]')
move_to_cart.click()

cart_page = driver.find_element(By.XPATH, '//a[@class="shopping_cart_link"]')
cart_page.click()

name_clothes_in_cart = driver.find_element(By.XPATH, '//div[@class="inventory_item_name"]')
clothes_in_cart = name_clothes_in_cart.text

price_in_cart = driver.find_element(By.XPATH, '//div[@class="inventory_item_price"]')
finish_price_in_cart = price_in_cart.text

print(f'{clothes_in_cart} - {finish_price_in_cart}')

assert actual_name_clothes == clothes_in_cart
assert actual_price == finish_price_in_cart

checkout = driver.find_element(By.XPATH, '//button[@id="checkout"]')
checkout.click()

# Заполняем информацию о покупателе
first_name = driver.find_element(By.XPATH, '//input[@id="first-name"]')
first_name.send_keys('M')

last_name = driver.find_element(By.XPATH, '//input[@id="last-name"]')
last_name.send_keys('S')

postal_code = driver.find_element(By.XPATH, '//input[@id="postal-code"]')
postal_code.send_keys('S-P')

checkout = driver.find_element(By.XPATH, '//input[@id="continue"]')
checkout.click()


price_in_cart_end = driver.find_element(By.XPATH, '//div[@class="summary_subtotal_label"]')
end_price_in_cart = price_in_cart_end.text
print(end_price_in_cart)

total_price = 'Item total: ' + actual_price
print(actual_price)
print(total_price)
# проверка по соответствию
assert total_price == end_price_in_cart

# проверка по включению
assert actual_price in end_price_in_cart
print('Test complete!')

actual_date = datetime.datetime.utcnow().strftime("%Y.%m.%d %H.%M.%S")
name_screenshot = 'smoketest_complete_' + actual_date + '.png'
driver.save_screenshot('D:\\games\\' + name_screenshot)

time.sleep(2)

driver.close()

# Скролл по окну вниз
# scroll_down = driver.execute_script("window.scrollTo(0, 40)")
# time.sleep(2)
#
# scroll_down_1 = driver.execute_script("window.scrollTo(0, 100)")
# time.sleep(2)
#
# scroll_down_2 = driver.execute_script("window.scrollTo(0, 130)")
# time.sleep(2)

# Переместиться к элементу (например для скриншота)
# move_to = ActionChains(driver)
# t_shirt = driver.find_element(By.XPATH, '//button[@id="add-to-cart-sauce-labs-onesie"]')
# move_to.move_to_element(t_shirt).perform()
# time.sleep(2)

# action = ActionChains(driver)
# slider = driver.find_element(By.XPATH, '//input[@class="range-slider range-slider--primary"]')
# action.click_and_hold(slider).move_to_element()
