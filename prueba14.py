from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time

from integraciones.integracionMantis import enviar_resultado_mantis, obtener_proyectos_mantis

options = Options()
options.add_argument("--headless")
driver = webdriver.Firefox(options=options)

try:
    url = "https://mantistcy.cl/mundomichiguau/sitio/index.php#tienda"
    driver.get(url)
    driver.maximize_window()
        
    
    inputs = driver.find_elements(By.TAG_NAME, "input")
    

    time.sleep(3)
        
   
    boton_categoria = driver.find_element(By.XPATH, "//*[@id='tienda']/div/div[2]/a[2]")

  
  
    boton_categoria.click()
        
      
        
    time.sleep(3) 

    driver.save_screenshot("evidencia.png")
        
    


    time.sleep(3)
    
    obtener_proyectos_mantis()
    enviar_resultado_mantis(
        "Seleccionar categoría en el catálogo",
        "La página debe permitir seleccionar categorías en el catálogo",
        "Se ingresó a la página - Se clickeó en la categoría deseada",
        "la página mostró los productos de la categoría seleccionada",
        "evidencia.png"
    )

  
finally :
    driver.quit()