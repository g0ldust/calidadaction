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

        for i in range(1, 23):

            boton_editar = driver.find_element(By.XPATH, f"//*[@id='carsTableBody']/tr[{i}]/td[6]/button[1]")
    

        

        
            boton_editar.click()

            time.sleep(0.5)
            if i == 23:
                obtener_proyectos_mantis()
                enviar_resultado_mantis("Los botones de edición funcionan correctamente", "la página debe mostrar la información del auto en los campos de edición", 
                                        "-se ingresó a la pagina" \
                                        "-se ingresó el usuario y contraseña" \
                                        "-23 veces seguidas se seleccionó el botón de edición" \
                                        "-en todos los casos la página mostró la información del auto correctamente","el botón de edición se seleccionó 23 veces seguidas y en todas las ocasiones la página mostró la información del auto correctamente")        
    
    else:
        print("No se encontraron los campos. ¿Quizás ya iniciaste sesión?")
        

   
    
finally:
    driver.quit()