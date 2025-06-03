#Antes de tudo precisaremos dos seguintes imports:
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

try:
  driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
  driver.get("https://demoblaze.com/")
  time.sleep(3)

  btn_login_up = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "login2")))
  btn_login_up.click()
  time.sleep(2)

  input_user = driver.find_element(By.ID, "loginusername")
  input_user.clear()
  input_user.send_keys("JoãoPedro")

  input_pass = driver.find_element(By.ID, "loginpassword")
  input_pass.clear()
  input_pass.send_keys("testeSenai1234")

  btn_confirm = driver.find_element(By.XPATH,"//button[contains(@class,'btn') and contains(text(),'Log in')]")
  btn_confirm.click()
  time.sleep(3)

  alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
  text = alert.text
  alert.accept()
  time.sleep(2)

  if text == "User does not exist":
    print("Cenário - Login com username correto e senha incorreta: Sucesso")
  else:
    print(f"Cenário - Login com username correto e senha incorreta: Falhou ({text})")

  #fechar o navegador
  driver.quit()

except Exception as e:
  print(f"Ocorreu um erro: {e}")