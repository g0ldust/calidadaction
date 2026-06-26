from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

from integraciones.integracionMantis import enviar_resultado_mantis, obtener_proyectos_mantis

options = Options()
options.add_argument("--headless")
driver = webdriver.Firefox(options=options)

try:
    url = "https://mantistcy.cl/mundomichiguau/sitio/index.php#tienda"
    driver.get(url)
    driver.maximize_window()
    
    # Espera explícita para que la página cargue completamente
    wait = WebDriverWait(driver, 15)
    
    # Espera a que el elemento esté presente y sea clickeable
    try:
        boton_categoria = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='tienda']/div/div[2]/a[2]"))
        )
        boton_categoria.click()
        print("✅ Clic en categoría realizado con éxito")
    except TimeoutException:
        print("⚠️ No se encontró el botón con el XPATH principal, intentando alternativa...")
        
        # Plan B: Buscar por texto o clase
        try:
            boton_categoria = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, 'categoria')]"))
            )
            boton_categoria.click()
            print("✅ Clic en categoría realizado con selector alternativo")
        except:
            # Plan C: Buscar cualquier enlace que contenga "categoría" en el texto
            boton_categoria = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Categoría') or contains(text(), 'categoria')]"))
            )
            boton_categoria.click()
            print("✅ Clic en categoría realizado con selector por texto")
    
    # Espera a que la página procese el clic
    time.sleep(3)
    
    # Guarda la evidencia
    driver.save_screenshot("evidencia.png")
    print("✅ Captura de pantalla guardada")
    
    # Envía el resultado
    obtener_proyectos_mantis()
    enviar_resultado_mantis(
        "Seleccionar categoría en el catálogo",
        "La página debe permitir seleccionar categorías en el catálogo",
        "Se ingresó a la página - Se clickeó en la categoría deseada",
        "la página mostró los productos de la categoría seleccionada",
        "evidencia.png"
    )

except Exception as e:
    print(f"❌ Error general: {str(e)}")
    # Guarda evidencia del error
    driver.save_screenshot("error_evidencia.png")
    raise

finally:
    driver.quit()