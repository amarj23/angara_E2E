from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get('https://www.angara.in')
time.sleep(5)
wait = WebDriverWait(driver,25)

driver.find_element(By.XPATH, '//*[@id="angara-jewellery-handcrafted-fine-jewellery-you-can-flaunt-every-day"]/div[13]/div/div[2]/div/div/div/div[2]/div/div[1]').click()
time.sleep(5)
driver.find_element(By.XPATH, '//*[@id="shopify-section-template--22971760115993__315ccfe1-972b-4ac2-98ad-90716143bd0b"]/div/div/article[4]/div/a/div').click()
ring = By.XPATH, '//*[@id="gf-products"]/div[2]/div/div[2]/div[1]'
wait.until(expected_conditions.presence_of_element_located(ring))

driver.find_element(By.XPATH, '//*[@id="gf-products"]/div[2]/div/div[2]/div[1]/a').click()
driver.find_element(By.XPATH, '//*[@id="option-box-1tem1"]/div[2]/span').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="option-box-1tem1"]/div[2]/ul/li[4]').click()
ring_Check_1 = driver.find_element(By.XPATH, '//*[@id="product-description"]/div/h1')
b = []
b.append(ring_Check_1.text)

driver.find_element(By.XPATH, '//*[@id="add-to-card-btn"]').click()
time.sleep(6)
ring_check_2 = driver.find_element(By.XPATH, '//*[@id="shopify-section-template--22971758346521__main"]/section/div[3]/form/div[1]/ul/li[3]/div/p[1]/a')
b.append(ring_check_2.text)

if b[0].lower() == b[1].lower():
    print('verified - item is added in cart')

driver.find_element(By.XPATH, "//*[@id= 'checkout']").click()
time.sleep(2)
driver.find_element(By.ID, 'email').send_keys('jujar.amar@gmail.com')
driver.find_element(By.XPATH, "//*[@id = 'TextField0']").send_keys('Amar')
# time.sleep(1)
driver.find_element(By.XPATH, "//*[@id = 'TextField1']").send_keys('Jujgar')
# time.sleep(1)
driver.find_element(By.XPATH, "//*[@id = 'shipping-address1']").send_keys('Pune')
# time.sleep(1)
driver.find_element(By.XPATH, "//*[@id = 'TextField2']").send_keys('Hadapsar')
# time.sleep(1)
driver.find_element(By.XPATH, "//*[@id = 'TextField3']").send_keys('Pune')
# time.sleep(1)
driver.find_element(By.XPATH, "//*[@id = 'TextField4']").send_keys('411028')
# time.sleep(1)
driver.find_element(By.XPATH, "//*[@id = 'TextField5']").send_keys('+918329623835')
# time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="Form0"]/div[1]/div/div/div[2]/div/div[2]/div[1]/button').click()
time.sleep(4)

if driver.find_element(By.XPATH, '//*[@id="Form2"]/div[1]/div/div/div/div/div[2]/div[1]/button').is_displayed():
    print('Test_case_001_Passed')
    driver.quit()
    assert True
else:
    print('Test_case_001_Failed')
    driver.quit()
    assert False