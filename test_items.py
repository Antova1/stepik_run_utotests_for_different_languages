import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


link ="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_button_add_to_card_exists_on_site(browser):
    browser.get(link)
    time.sleep(8)
    browser.implicitly_wait(8)
    button=browser.find_element(By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.btn-add-to-basket")
    button.click()
    time.sleep(8)
    input4 = WebDriverWait(browser, 15).until(EC.visibility_of_element_located((By.CSS_SELECTOR, " div.alertinner strong")))
    input5 = input4.text
    time.sleep(15)
    assert "Coders at Work" ==  input5, "Wrong answer"
