from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def ejecutar_prueba_sistema():

    options = Options()
    driver = webdriver.Chrome(options=options)

    try:
        driver.get("https://fundacion-instituto-profesional-duoc-uc.github.io/APIAutos/index.html")
        driver.maximize_window()
        SLEEP_TIME = 2
        time.sleep(SLEEP_TIME)
        print("titulo de la página: ", driver.title)
        titulo = driver.title

        inputs = driver.find_elements(By.TAG_NAME, "input")
        botones = driver.find_elements(By.TAG_NAME, "button")

        driver.save_screenshot("evidencia.png")
        detalle = f"""paso a paso ejecutado:
        1. se abrió la URL automaticamente
        2. Titulo Obtenido: {titulo}
        3. inputs encontrados: {len(inputs)}
        4. botones encontrados: {len(botones)}
        5. la pagina cargó correctamente"""

        print(f"Inputs encontrados: {len(inputs)}")
        print(f"Botones encontrados: {len(botones)}")

        if len(inputs) > 0 or len(botones) > 0:
            print("Se encontraron inputs y/o botones en la página.")
            return True, "La página cargó correctamente", detalle
        else:
            print("No se encontraron inputs ni botones en la página.")
            return False, "La página no cargó correctamente", detalle   
    except Exception as e:
        print(f"Error al abrir la página: ",e)
    finally:
        driver.quit()
        