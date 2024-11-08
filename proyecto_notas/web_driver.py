from selenium import webdriver

def wd_driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument("--start-maximized")
    wd = webdriver.Chrome(options=options)
    return wd

def go_login(wd):
    wd.get("https://uniempresarial.datasae.co/siga_new/web/app.php/login_responsive")