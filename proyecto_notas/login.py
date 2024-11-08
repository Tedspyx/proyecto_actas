from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

def click_captcha(wd):
    try:
        # Cambia al contexto del iframe que contiene el CAPTCHA
        iframe = WebDriverWait(wd, 20).until(
            EC.presence_of_element_located((By.XPATH, "//iframe[@title='reCAPTCHA']"))
        )
        wd.switch_to.frame(iframe)

        # Espera hasta que el checkbox del CAPTCHA sea clickeable
        captcha = WebDriverWait(wd, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='rc-anchor-center-item rc-anchor-checkbox-holder']//span[@id='recaptcha-anchor']//div[@class='recaptcha-checkbox-border']"))
        )
        captcha.click()

        # Vuelve al contexto principal
        wd.switch_to.default_content()
    except Exception as e:
        print("Error al dar click en el captcha:", e)

    
def login(wd,email,password):
    try:
        email_input = WebDriverWait(wd, 20).until(
            EC.visibility_of_element_located((By.ID, "txt_username-inputEl"))
        )
        email_input.send_keys(email)
        email_input.send_keys(Keys.ENTER)
        
        password_input = WebDriverWait(wd, 20).until(
            EC.visibility_of_element_located((By.ID, "txt_password-inputEl"))
        )
        password_input.send_keys(password)
        password_input.send_keys(Keys.ENTER)    
    finally:
        login_button = WebDriverWait(wd, 20).until(
            EC.element_to_be_clickable((By.ID,"login_button-btnEl"))
        )
        login_button.click()