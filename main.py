from test.integridadLogin import ejecutar_prueba_sistema
from integraciones.integracionMantis import obtener_proyectos_mantis, enviar_resultado_mantis


def main():
    obtener_proyectos_mantis()
    exito, mensaje, detalle = ejecutar_prueba_sistema()
    print(mensaje)
    codigo,respuesta = enviar_resultado_mantis("Resultado prueba automatizada", mensaje, detalle)
    print("mantis respondió", codigo, respuesta)

if __name__ == "__main__":
    main()