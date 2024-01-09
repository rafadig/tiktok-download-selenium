from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


url = "https://snaptik.app/"
driver = webdriver.Chrome()
driver.get(url)

def realizar_acoes(link):
    url_input = driver.find_element(By.ID, "url")
    url_input.clear()
    url_input.send_keys(link)

 
    download_button = driver.find_element(By.CLASS_NAME, "button-go")
    download_button.click()

 
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "download-file")))

 
    download_modal_button = driver.find_element(By.CLASS_NAME, "download-file")
    download_modal_button.click()

   
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "modal-close")) or
        EC.presence_of_element_located((By.CLASS_NAME, "download-file"))
    )

  
    if EC.presence_of_element_located((By.CLASS_NAME, "modal-close")):
        close_ad_button = driver.find_element(By.CLASS_NAME, "modal-close")
        close_ad_button.click()

      
        WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, "//span[text()='Download Completed']"))
        )

link_teste = "LINK DO VÍDEO"

realizar_acoes(link_teste)

driver.quit()
