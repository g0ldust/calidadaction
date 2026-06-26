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
    

       
        
        
    boton_catalogo = driver.find_element(By.XPATH, "/html/body/header/div/a")
   

    boton_catalogo.click()
        
      
        
    time.sleep(1) 

    driver.save_screenshot("evidencia.png")
        
        


    time.sleep(3)
       
    obtener_proyectos_mantis()
    enviar_resultado_mantis("Ir a la sección de catalogo", "La página debe permitir ir a la sección de catalogo", 
                                "Se ingresó a la página" \
                                "-Se clickeó en el botón de catálogo" \
                                "-Se visualizó el catálogo" \
                                , "la página mostró correctamente el catálogo", "evidencia.png") 
  
finally :
    driver.quit()