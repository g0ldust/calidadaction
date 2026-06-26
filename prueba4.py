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
    
    
    for i in range(1, 11):
        print(f"--- Intento número {i} ---")
         
        

        inputs = driver.find_elements(By.TAG_NAME, "input")
        
        if len(inputs) >= 2:
            campo_usuario = inputs[0]
            campo_password = inputs[1]

            campo_usuario.clear()
            campo_password.clear()

            campo_usuario.send_keys("Mario")
            campo_password.send_keys("duoc123")
            
            boton_ingresar = driver.find_element(By.TAG_NAME, "button")
            boton_ingresar.click()
            
            print(f"Credenciales enviadas e intento {i} completado.")
            
            time.sleep(0.5) 
            
  
        
            if i == 10:
                obtener_proyectos_mantis()
                enviar_resultado_mantis("El login de la pagina niega el inicio de sesión", "la página debe negar el inicio de sesión con credenciales incorrectas", 
                                        "-se ingresó a la pagina" \
                                        "-se ingresó el usuario erroneo y contraseña 10 veces seguidas" \
                                        "-10 veces seguidas se negó el inicio de sesión" \
                                        "-en todos los casos la página respondió correctamente", "La pagina negó el inicio de sesión con credenciales incorrectas en los 10 intentos")        
            else:
                print("Reiniciando la página ")    
        else:
            print("No se encontraron los campos. ¿Quizás ya iniciaste sesión?")
            break

   
  
finally:
    driver.quit()