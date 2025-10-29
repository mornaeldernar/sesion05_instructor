# Archivo: demo_02_funciones_avanzadas.py
"""
Demo 2: Funciones Avanzadas
Objetivo: Mostrar conceptos avanzados de funciones como args, kwargs y funciones anidadas
"""

def demo_funciones_avanzadas():
    print("=== Demo: Funciones Avanzadas ===")
    
    # Ejemplo 1: Args para número variable de argumentos
    def sumar_precios(*args):
        return sum(args)
    
    # Ejemplo 2: Kwargs para argumentos nombrados
    def crear_producto(**kwargs):
        return kwargs

    
    # Ejemplo 3: Función anidada
    def calcular_descuentos(precios):
        
        def aplicar_descuento(precio, porcentaje):
            return precio * (1 - porcentaje)
        descuentos = []
        for precio in precios:
            if precio >= 100:
                descuentos.append(aplicar_descuento(precio, 0.2))
            else:
                descuentos.append(aplicar_descuento(precio, 0.1))
        return descuentos
    
    # Demostración de uso
    print("\nEjemplo 1: Args")
    total = sumar_precios(100, 200, 300,500,100,231,50,127,47,102,23)
    print(f"Suma total: ${total}")
    
    print("\nEjemplo 2: Kwargs")
    producto = crear_producto(nombre="Laptop", precio=1200, categoria="Electrónica")
    print("Producto creado:", producto)
    
    print("\nEjemplo 3: Función anidada")
    precios = [80, 120, 200]
    precios_con_descuento = calcular_descuentos(precios)
    print("Precios originales:", precios)
    print("Precios con descuento:", precios_con_descuento)
    print(aplicar_descuento(200,0.1))
if __name__ == "__main__":
    demo_funciones_avanzadas()