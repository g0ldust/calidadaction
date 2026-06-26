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
    

       
        
        
   
    boton_anadir = driver.find_element(By.XPATH, "//*[@id='tienda']/div/div[3]/div[1]/div/div/div/a")
    

  
  
    boton_anadir.click()
    boton_carrito = driver.find_element(By.XPATH, "//*[@id='navbarNav']/ul/li[2]/a")
    boton_carrito.click()
      
        
    time.sleep(3) 

    driver.save_screenshot("evidencia.png")
        
    


    time.sleep(3)
    obtener_proyectos_mantis()
    enviar_resultado_mantis(
        "Seleccionar boton de agregar al carrito",
        "La página debe permitir agregar productos al carrito al hacer clic en el botón de agregar",
        "Se ingresó a la página - Se clickeó en el botón de agregar al carrito - Se clickeó en el botón de carrito",
        "la página mostró el producto agregado correctamente",
        "evidencia.png"
    )
   

  
finally :
    driver.quit()