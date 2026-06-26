
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

options = Options()
driver = webdriver.Chrome(options=options)

try:
    driver.get("https://fundacion-instituto-profesional-duoc-uc.github.io/APIAutos/index.html")
    driver.maximize_window()
    SLEEP_TIME = 2
    time.sleep(SLEEP_TIME)
    print("titulo de la página: ", driver.title)

    inputs = driver.find_elements(By.TAG_NAME, "input")
    botones = driver.find_elements(By.TAG_NAME, "button")
    print(f"Inputs encontrados: {len(inputs)}")
    print(f"Botones encontrados: {len(botones)}")

    if len(inputs) > 0 or len(botones) > 0:
        print("Se encontraron inputs y/o botones en la página.")
    else:
        print("No se encontraron inputs ni botones en la página.")
except Exception as e:
    print(f"Error al abrir la página: ",e)
finally:
    driver.quit()
    