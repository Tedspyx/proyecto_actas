from web_driver import *
from login import *
from navigation import *


def main():
    wd = wd_driver()
    go_login(wd)     
    click_captcha(wd) 
    login(wd,"99123011086","Colombia.1997")

    try:
        click_hoja(wd)
        
        change_to_iframe(wd)
        
        academy_button(wd)
    except:
        print("Error")
        
if __name__ == '__main__':
    main()