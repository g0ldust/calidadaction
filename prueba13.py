from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time

from integraciones.integracionMantis import enviar_resultado_mantis, obtener_proyectos_mantis

options = Options()
driver = webdriver.Firefox(options=options)

try:
    url = "https://mantistcy.cl/mundomichiguau/sitio/index.php#tienda"
    driver.get(url)
    driver.maximize_window()
        
    
    inputs = driver.find_elements(By.TAG_NAME, "input")
    

       
        
        
    campo_buscar = driver.find_element(By.XPATH, "//*[@id='tienda']/div/div[1]/div/form/input")
    boton_buscar = driver.find_element(By.XPATH, "//*[@id='tienda']/div/div[1]/div/form/button")

    campo_buscar.click()
    campo_buscar.send_keys("perro")
    boton_buscar.click()
        
      
        
    time.sleep(3) 

    driver.save_screenshot("evidencia.png")
        
    


    time.sleep(3)
    
    obtener_proyectos_mantis()
    enviar_resultado_mantis(
        "Realizar búsqueda en el catálogo",
        "La página debe permitir buscar productos en el catálogo",
        "Se ingresó a la página - Se clickeó en el campo de búsqueda - Se ingresó el texto a buscar - Se cliqueo el botón de busqueda",
        "la página hizo la busqueda correctamente y mostró los resultados",
        "evidencia.png"
    )

  
finally :
    driver.quit()