from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

def click_hoja(wd):
    click_hoja = WebDriverWait(wd, 20).until(
        EC.presence_of_element_located((By.ID,"ext-element-7"))
    )
    click_hoja.click()
    
def change_to_iframe(wd):
        iframe = WebDriverWait(wd, 20).until(
        EC.presence_of_element_located((By.XPATH, "//iframe[@id='panel_extModel9-1']"))
    )
        print("Iframe encontrado")
        wd.switch_to.frame(iframe)
        
def academy_button(wd):
    academy_button = WebDriverWait(wd, 40).until(
        EC.visibility_of_element_located((By.XPATH,"//a[@id='tab-1348']//span[@id='tab-1348-btnWrap']//span[@id='tab-1348-btnEl']//span[@id='tab-1348-btnInnerEl']"))
    )
    academy_button.click()