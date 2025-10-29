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
    if not args:
        return {"error": "No hay ventas para procesar"} 
    # 2. Crear diccionario para resultados
    resultados = {}
    # 3. Si kwargs['calcular_total']: calcular suma total
    if kwargs['calcular_total']:
        resultados['total'] = sum(args)
    # 4. Si kwargs['encontrar_maximo']: encontrar venta máxima
    if kwargs.get('encontrar_maximo'):
        resultados['maximo'] = max(args) if args else 0
    # 5. Si kwargs['contar_superiores']: contar ventas > umbral
    if kwargs.get('contar_superiores'):
        umbral = kwargs.get('umbral', 0)
        superiores = []
        for valor in args:
            if valor > umbral:
                superiores.append(1)
        superiores2= [1 for valor in args if valor > umbral]
        print(superiores)
        print(superiores2)
        print(sum(superiores))
        print(sum(superiores2))

        resultados['superiores'] = sum(1 for v in args if v > umbral)

    return resultados

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
        resultado2 = procesar_ventas(*ventas, contar_superiores=True, encontrar_maximo=True, umbral=200, calcular_total=True)
        print("\nCaso 2 - Ventas superiores a $200:")
        print(f"Resultados: {resultado2}")
        
    except NotImplementedError as e:
        print(f"\nEstado: {str(e)}")

if __name__ == "__main__":
    main()