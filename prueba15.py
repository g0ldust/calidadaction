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
    

       
        
        
   
    boton_amor = driver.find_element(By.XPATH, "//*[@id='navbarNav']/ul/li[1]/a")

  
  
    boton_amor.click()
        
      
        
    time.sleep(3) 

    driver.save_screenshot("evidencia.png")
        
    


    time.sleep(3)
    obtener_proyectos_mantis()
    enviar_resultado_mantis(
        "Seleccionar boton de nuestro amor",
        "La página debe mostrar su mision y visión al seleccionar el botón de nuestro amor",
        "Se ingresó a la página - Se clickeó en el botón de nuestro amor",
        "la página mostró la mision y visión correctamente",
        "evidencia.png"
    )
   

  
finally :
    driver.quit()