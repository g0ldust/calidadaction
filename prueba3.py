from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time

from integraciones.integracionMantis import enviar_resultado_mantis, obtener_proyectos_mantis

options = Options()
driver = webdriver.Firefox(options=options)

try:
    url = "https://fundacion-instituto-profesional-duoc-uc.github.io/APIAutos/index.html"
    driver.get(url)
    driver.maximize_window()
        
    
    inputs = driver.find_elements(By.TAG_NAME, "input")
    
    if len(inputs) >= 2:
        campo_usuario = inputs[0]
        campo_password = inputs[1]

        
        campo_usuario.clear()
        campo_password.clear()

        
        campo_usuario.send_keys("duoc")
        campo_password.send_keys("duoc123")
        
        
        boton_ingresar = driver.find_element(By.TAG_NAME, "button")
        boton_ingresar.click()
        
      
        
        time.sleep(5) 
        CAMPO_ANNO = driver.find_element(By.XPATH, "//*[@id='anio']")
        CAMPO_ANNO.send_keys("e.-")

        time.sleep(1)
        obtener_proyectos_mantis()
        enviar_resultado_mantis("El campo de año se llena solo con numeros", "El campo de año debe aceptar solo números y no letras ni caracteres especiales", 
                                "-se ingresó a la pagina" \
                                "-se ingresó el usuario y contraseña" \
                                "-se ingresó el año con letras y caracteres especiales" \
                                "-la pagina permitió ingresar el año con letras y caracteres especiales","el campo de año no permitió ingresar letras y caracteres especiales")    

    else:
        print("No se encontraron los campos. ¿Quizás ya iniciaste sesión?")
        

   
    
finally:
    driver.quit()