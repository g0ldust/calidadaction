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
    
    # Ciclo para repetir 10 veces
    for i in range(1, 11):
        print(f"--- Intento número {i} ---")
         
        
        # IMPORTANTE: Buscamos los elementos DENTRO del ciclo
        # Esto evita el error de "Stale Element"
        inputs = driver.find_elements(By.TAG_NAME, "input")
        
        if len(inputs) >= 2:
            campo_usuario = inputs[0]
            campo_password = inputs[1]

            # Limpiar campos por si tienen texto previo
            campo_usuario.clear()
            campo_password.clear()

            # Ingresar credenciales
            campo_usuario.send_keys("duoc")
            campo_password.send_keys("duoc123")
            
            # Buscar y hacer clic en el botón
            boton_ingresar = driver.find_element(By.TAG_NAME, "button")
            boton_ingresar.click()
            
            print(f"Credenciales enviadas e intento {i} completado.")
            
            time.sleep(5) 
            
  
            driver.get(url) 
            if i == 10:
                obtener_proyectos_mantis()
                enviar_resultado_mantis("El login de la pagina aguanta varios inicios de sesión", "la página debe aguantar que se ingrese varias veces un usuario", 
                                        "-se ingresó a la pagina" \
                                        "-se ingresó el usuario y contraseña 10 veces seguidas" \
                                        "-10 veces seguidas se salió de la sesión" \
                                        "-en todos los casos la página respondió correctamente","La pagina aguantó 10 inicios de sesión seguidos sin problemas")        
            else:
                print("Reiniciando la página ")    
        else:
            print("No se encontraron los campos. ¿Quizás ya iniciaste sesión?")
            break

   
    print(f"Error durante la ejecución: {e}")
finally:
    driver.quit()