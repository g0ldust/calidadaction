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
        
      
        
        time.sleep(3) 
        boton_bajar = driver.find_element(By.XPATH, "//*[@id='precio']")
        boton_bajar.send_keys("-1000000")

        time.sleep(1)
        obtener_proyectos_mantis()
        enviar_resultado_mantis("Crear autos con precio negativo", "La página no debe permitir ingresar un precio negativo al crear o editar un auto", 
                                "-se ingresó a la pagina" \
                                "-se ingresó el usuario y contraseña" \
                                "-se ingresó un precio negativo" \
                                "-la pagina permitió ingresar el precio negativo", "la página no permitió ingresar un precio negativo al crear o editar un auto")    

    else:
        print("No se encontraron los campos. ¿Quizás ya iniciaste sesión?")
finally :
    driver.quit()