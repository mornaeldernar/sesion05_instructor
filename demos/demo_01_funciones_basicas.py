# Archivo: demo_01_funciones_basicas.py
"""
Demo 1: Funciones Básicas
Objetivo: Mostrar la definición y uso básico de funciones en Python
"""

def demo_funciones_basicas():
    print("=== Demo: Funciones Básicas ===")
    
    # Ejemplo 1: Función simple
    def saludar(nombre):
        return f"¡Hola, {nombre}!"
    
    # Ejemplo 2: Función con múltiples parámetros
    def calcular_total(precio, cantidad):
        return precio * cantidad
    
    # Ejemplo 3: Función con valor por defecto
    def aplicar_descuento(precio, descuento=0.1):
        return precio * (1 - descuento)
    
    # Demostración de uso
    print("\nEjemplo 1: Función simple")
    print(saludar("Ana"))
    
    print("\nEjemplo 2: Función con múltiples parámetros")
    total = calcular_total(100,2)
    print(f"Total de la compra: ${total}")
    
    print("\nEjemplo 3: Función con valor por defecto")
    precio_final = aplicar_descuento(200)
    print(f"Precio con descuento: ${precio_final}")

if __name__ == "__main__":
    demo_funciones_basicas()
