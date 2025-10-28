# Archivo: lab_02_procesador.py
"""
Laboratorio 2: Procesador de Ventas
Objetivo: Practicar funciones avanzadas y manipulación de datos

La función debe:
1. Procesar una lista de ventas con args
2. Aplicar diferentes análisis según kwargs
3. Retornar un diccionario con los resultados
"""

def procesar_ventas(*args, **kwargs):
    """
    Procesa una lista de ventas y realiza análisis según los parámetros
    Args:
        *args: Lista de montos de ventas
        **kwargs: Opciones de análisis (calcular_total, encontrar_maximo, etc.)
    Returns:
        dict: Resultados de los análisis solicitados
    Raises:
        NotImplementedError: Cuando el estudiante aún no implementa
    """
    # TODO: Implementar el procesamiento siguiendo estos pasos:
    # 1. Validar que haya ventas para procesar
    # 2. Crear diccionario para resultados
    # 3. Si kwargs['calcular_total']: calcular suma total
    # 4. Si kwargs['encontrar_maximo']: encontrar venta máxima
    # 5. Si kwargs['contar_superiores']: contar ventas > umbral
    
    raise NotImplementedError("¡Función no implementada!")

def main():
    # Casos de prueba
    ventas = [100, 200, 300, 150, 250]
    
    print("=== Procesador de Ventas ===")
    print(f"Ventas a procesar: {ventas}")
    
    try:
        # Caso 1: Calcular total y máximo
        resultado1 = procesar_ventas(*ventas, calcular_total=True, encontrar_maximo=True)
        print("\nCaso 1 - Total y Máximo:")
        print(f"Resultados: {resultado1}")
        
        # Caso 2: Contar ventas superiores
        resultado2 = procesar_ventas(*ventas, contar_superiores=True, umbral=200)
        print("\nCaso 2 - Ventas superiores a $200:")
        print(f"Resultados: {resultado2}")
        
    except NotImplementedError as e:
        print(f"\nEstado: {str(e)}")

if __name__ == "__main__":
    main()