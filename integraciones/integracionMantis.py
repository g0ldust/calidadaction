import base64
import os
import requests

TOKEN = "tTsTutZHwXs2KgikVeX8kLVaMGXiYoIj"
BASE_URL = "https://mantistcy.cl/mantis/api/rest/issues"


# --- 1. FUNCIÓN PARA OBTENER PROYECTOS ---
def obtener_proyectos_mantis():
    headers = {"Authorization": TOKEN}
    response = requests.get(BASE_URL, headers=headers)
    print(response.status_code)
    print(response.text)
    return response.status_code, response.text


# --- 2. FUNCIÓN PARA ENVIAR EL REPORTE CON LA IMAGEN ---
def enviar_resultado_mantis(
    resumen, descripcion, detalle, esperado, nombre_imagen
):
    headers = {"Authorization": TOKEN, "Content-Type": "application/json"}

    # Localizar la imagen en la raíz del proyecto
    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    raiz_proyecto = os.path.dirname(directorio_actual)
    ruta_completa_imagen = os.path.join(raiz_proyecto, nombre_imagen)

    # Leer la imagen y codificarla en Base64
    try:
        with open(ruta_completa_imagen, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode(
                "utf-8"
            )
    except FileNotFoundError:
        print(
            f"Error: No se encontró la imagen en la ruta: {ruta_completa_imagen}"
        )
        return None, "Archivo no encontrado"

    # Estructura del JSON para Mantis
    payload = {
        "summary": resumen,
        "description": descripcion,
        "project": {
            "name": "grupo1 - Reyes - Toledo - Zuñiga - Mella - Rodriguez - Contreras"
        },
        "category": {"name": "Caja Negra"},
        "custom_fields": [
            {"field": {"name": "Resultado Esperado"}, "value": esperado},
            {"field": {"name": "Tipo Prueba"}, "value": "Funcional "},
            {"field": {"name": "Resultado Obtenido"}, "value": detalle},
        ],
        "files": [{"name": nombre_imagen, "content": encoded_string}],
    }

    # Enviar reporte
    response = requests.post(BASE_URL, json=payload, headers=headers)
    return response.status_code, response.text