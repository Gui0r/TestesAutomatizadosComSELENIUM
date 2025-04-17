from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    driver.get("https://www.saucedemo.com/")
    time.sleep(2)

    login_field = driver.find_element(By.ID, "user-name")
    login_field.send_keys("invalid_user")

    senha_field = driver.find_element(By.ID, "password")
    senha_field.send_keys("wrong_password")

    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()

    time.sleep(2)
    
    mensagem_erro = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")
    print(mensagem_erro.text)
    
    
except Exception as e:
    print(f"Erro: {e}")

finally:
    driver.quit()



