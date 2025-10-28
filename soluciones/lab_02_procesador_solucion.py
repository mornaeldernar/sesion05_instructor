# Archivo: lab_02_procesador_solucion.py
"""
Laboratorio 2: Procesador de Ventas (SOLUCIÓN)
Objetivo: Practicar funciones avanzadas y manipulación de datos
"""

def procesar_ventas(*args, **kwargs):
    """
    Procesa una lista de ventas y realiza análisis según los parámetros
    Args:
        *args: Lista de montos de ventas
        **kwargs: Opciones de análisis (calcular_total, encontrar_maximo, etc.)
    Returns:
        dict: Resultados de los análisis solicitados
    """
    # Validar que haya ventas
    if not args:
        return {"error": "No hay ventas para procesar"}
    
    # Inicializar resultados
    resultados = {}
    
    # Calcular total si se solicita
    if kwargs.get('calcular_total'):
        resultados['total'] = sum(args)
    
    # Encontrar máximo si se solicita
    if kwargs.get('encontrar_maximo'):
        resultados['maximo'] = max(args)
    
    # Contar ventas superiores si se solicita
    if kwargs.get('contar_superiores'):
        umbral = kwargs.get('umbral', 0)
        resultados['superiores_a_umbral'] = len([v for v in args if v > umbral])
    
    return resultados

def main():
    # Casos de prueba
    ventas = [100, 200, 300, 150, 250]
    
    print("=== Procesador de Ventas ===")
    print(f"Ventas a procesar: {ventas}")
    
    # Caso 1: Calcular total y máximo
    resultado1 = procesar_ventas(*ventas, calcular_total=True, encontrar_maximo=True)
    print("\nCaso 1 - Total y Máximo:")
    print(f"Resultados: {resultado1}")
    
    # Caso 2: Contar ventas superiores
    resultado2 = procesar_ventas(*ventas, contar_superiores=True, umbral=200)
    print("\nCaso 2 - Ventas superiores a $200:")
    print(f"Resultados: {resultado2}")

if __name__ == "__main__":
    main()