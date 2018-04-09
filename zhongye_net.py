from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument("--headless")
prefs = {"profile.managed_default_content_settings.images":2}
chromeOptions.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(chrome_options=chromeOptions)
driver.get('http://www.zhongye.net/login.htm')
# user login
driver.find_element_by_name("username").send_keys("18812345678")
driver.find_element_by_name("password").send_keys("123456")
driver.find_element_by_id("loginBtn").click()
# wait for page loading
WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CLASS_NAME, 'usml_qiandao')))
# sign in
driver.find_element_by_xpath('//*[@id="form1"]/div[5]/div[1]/div/div[2]/a[1]').click()
# wait for alert dialog
WebDriverWait(driver, 3).until(EC.alert_is_present())
# press OK
driver.switch_to.alert.accept()
driver.quit()
