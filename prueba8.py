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
        campo_anio = driver.find_element(By.XPATH, "//*[@id='anio']")
        campo_anio.send_keys("2048")
        campo_idmarca = driver.find_element(By.XPATH, "//*[@id='marca_id']")
        campo_idmarca.send_keys("2")
        campo_modelo = driver.find_element(By.XPATH, "//*[@id='modelo']")
        campo_modelo.send_keys("Corolla")
        campo_precio = driver.find_element(By.XPATH, "//*[@id='precio']")
        campo_precio.send_keys("10000000")
        boton_guardar = driver.find_element(By.XPATH, "//*[@id='saveCarBtn']")
        boton_guardar.click()

        time.sleep(1)
        obtener_proyectos_mantis()
        enviar_resultado_mantis("Crear autos con año mayor a 2027", "La página no debe permitir ingresar un año mayor a 2027 al crear o editar un auto", 
                                "-se ingresó a la pagina" \
                                "-se ingresó el usuario y contraseña" \
                                "-se ingresó un año mayor a 2027" \
                                "-la pagina permitió ingresar el año mayor a 2027", "la página no permitió ingresar un año mayor a 2027 al crear o editar un auto")    

    else:
        print("No se encontraron los campos. ¿Quizás ya iniciaste sesión?")
finally :
    driver.quit()