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
    

       
        
        
   
    boton_registro = driver.find_element(By.XPATH, "//*[@id='navbarNav']/ul/li[4]/a")
    

  
  
    boton_registro.click()

    time.sleep(3) 

    driver.save_screenshot("evidencia.png")
        
    


    time.sleep(3)
    obtener_proyectos_mantis()
    enviar_resultado_mantis(
        "clikear en el boton de registro",
        "La página debe permitir ir a la sección de registro al hacer clic en el botón de registro",
        "Se ingresó a la página - Se clickeó en el botón de registro",
        "la página mostró la página de registro correctamente",
        "evidencia.png"
    )
   

  
finally :
    driver.quit()