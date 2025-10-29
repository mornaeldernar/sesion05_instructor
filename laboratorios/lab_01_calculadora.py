# Archivo: lab_01_calculadora.py
"""
Laboratorio 1: Calculadora de Precios
Objetivo: Practicar la creación de funciones básicas

La función debe:
1. Calcular el precio final con IVA
2. Aplicar descuento si corresponde
3. Validar que los valores sean positivos
"""

def calcular_precio_final(precio_base, cantidad, descuento=0):
    """
    Calcula el precio final de una compra incluyendo IVA y descuento
    Args:
        precio_base (float): Precio unitario del producto
        cantidad (int): Cantidad de unidades
        descuento (float): Porcentaje de descuento (0-1)
    Returns:
        float: Precio final después de IVA y descuento
    Raises:
        NotImplementedError: Cuando el estudiante aún no implementa
        ValueError: Cuando los valores son inválidos
    """
    # TODO: Implementar el cálculo siguiendo estos pasos:
    # 1. Validar que precio_base y cantidad sean positivos
    if precio_base < 0:
        raise ValueError("El precio base debe ser un valor positivo.")
    if cantidad < 0:
        raise ValueError("La cantidad debe ser un valor positivo.")
    # 2. Validar que descuento esté entre 0 y 1
    if not (0 <= descuento <= 1):
        raise ValueError("El descuento debe estar entre 0 y 1.")
    # 3. Calcular subtotal (precio_base * cantidad)
    subtotal = precio_base * cantidad
    # 4. Aplicar descuento si existe
    if descuento > 0:
        subtotal = subtotal * (1 - descuento)
    # 5. Agregar IVA (19%)
    total = subtotal * 1.19
    return total
    

def main():
    # Casos de prueba
    print("=== Calculadora de Precios ===")
    
    try:
        # Caso 1: Sin descuento
        precio1 = calcular_precio_final(-100, 2)
        print(f"\nCaso 1 - Precio base: $100, Cantidad: 2")
        print(f"Precio final: ${precio1}")
        
        # Caso 2: Con descuento
        precio2 = calcular_precio_final(100, 2, 0.1)
        print(f"\nCaso 2 - Precio base: $100, Cantidad: 2, Descuento: 10%")
        print(f"Precio final: ${precio2}")
        
    except NotImplementedError as e:
        print(f"\nEstado: {str(e)}")
    except ValueError as e:
        print(f"\nError: {str(e)}")

if __name__ == "__main__":
    main()