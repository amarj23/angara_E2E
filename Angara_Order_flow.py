from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get('https://www.angara.in')
time.sleep(5)
wait = WebDriverWait(driver,25)
# print(driver.find_element(By.XPATH, '//*[@id="angara-jewellery-handcrafted-fine-jewellery-you-can-flaunt-every-day"]/div[13]/div/div[2]/div/div/div/div[2]/div/div[1]').is_displayed())

driver.find_element(By.XPATH, '//*[@id="angara-jewellery-handcrafted-fine-jewellery-you-can-flaunt-every-day"]/div[13]/div/div[2]/div/div/div/div[2]/div/div[1]').click()
time.sleep(5)
driver.find_element(By.XPATH,
                    '//*[@id="shopify-section-template--22952685011225__315ccfe1-972b-4ac2-98ad-90716143bd0b"]/div/div/article[4]/div/a/div').click()
ring = By.XPATH, '//*[@id="gf-products"]/div[2]/div/div[2]/div[1]'
wait.until(expected_conditions.presence_of_element_located(ring))

driver.find_element(By.XPATH, '//*[@id="gf-products"]/div[2]/div/div[2]/div[1]/a').click()
driver.find_element(By.XPATH, '//*[@id="option-box-1tem1"]/div[2]/span').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="option-box-1tem1"]/div[2]/ul/li[4]/a').click()

driver.find_element(By.XPATH, '//*[@id="8818607391001-product-form-buttons-template--22952686387481__main"]/div[3]').click()
time.sleep(4)
driver.find_element(By.XPATH, '//*[@id="shopify-section-template--22952683274521__main"]/section/div[3]/form/div[3]/div[2]').click()
time.sleep(2)
driver.find_element(By.ID, 'email').send_keys('jujar.amar@gmail.com')
if driver.find_element(By.ID, 'checkout-main-header').is_displayed():
    print('Test_case_001_Passed')
    assert True
else:
    print('Test_case_001_Failed')
    assert False
