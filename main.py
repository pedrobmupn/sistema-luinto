import os

class Producto:
    def __init__(self, nombre, precio, stock, stock_min, categoria):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.stock_min = stock_min
        self.categoria = categoria

    def __str__(self):
        return (f"  {self.nombre:<20} | S/. {self.precio:>6.2f} "
                f"| Stock: {self.stock:>4} | Min: {self.stock_min:>3} "
                f"| {self.categoria}")

class Venta:
    def __init__(self, nombre_producto, cantidad, subtotal):
        self.nombre_producto = nombre_producto
        self.cantidad = cantidad
        self.subtotal = subtotal

productos = []
ventas = []

ARCHIVO = "bodega.txt"

def validar_numero(mensaje, tipo=float, minimo=None):
    while True:
        entrada = input(mensaje).strip()
        if not entrada:
            print("  No puede estar vacío. Intente de nuevo.")
            continue
        try:
            valor = tipo(entrada)
            if minimo is not None and valor < minimo:
                print(f"  El valor debe ser >= {minimo}. Intente de nuevo.")
            else:
                return valor
        except ValueError:
            print("  Debe ingresar un número válido. Intente de nuevo.")

def cargar_datos():
    global productos
    if not os.path.exists(ARCHIVO):
        print("  Info: No se encontró archivo. Iniciando vacío.")
        return
    with open(ARCHIVO, "r", encoding="utf-8") as f:
        for linea in f:
            partes = linea.strip().split("|")
            if len(partes) == 5:
                nombre = partes[0]
                precio = float(partes[1])
                stock = int(partes[2])
                stock_min = int(partes[3])
                categoria = partes[4]
                productos.append(Producto(nombre, precio, stock, stock_min, categoria))
    print(f"  {len(productos)} producto(s) cargado(s) desde archivo.")

def guardar_datos():
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        for p in productos:
            f.write(f"{p.nombre}|{p.precio}|{p.stock}|{p.stock_min}|{p.categoria}\n")
    print(f"  Datos guardados en '{ARCHIVO}'.")

def agregar_producto():
    print("\n--- Agregar Nuevo Producto ---")
    nombre = input("  Nombre del producto: ").strip()
    if not nombre:
        print(" El nombre no puede estar vacío.")
        return
    for p in productos:
        if p.nombre.lower() == nombre.lower():
            print(" Ya existe un producto con ese nombre.")
            return
    precio = validar_numero(" Precio unitario (S/.): ", float, 0.01)
    stock = validar_numero(" Stock inicial : ", int, 0)
    stock_min = validar_numero("  Stock mínimo : ", int, 0)
    categoria = input("Categoría: ").strip() or "General"
    productos.append(Producto(nombre, precio, stock, stock_min, categoria))
    print(f"Producto '{nombre}' agregado correctamente.")

def registrar_venta():
    print("\n--- Registrar Venta ---")
    if not productos:
        print("No hay productos en el catálogo.")
        return
    nombre_buscado = input("Nombre del producto: ").strip()
    producto_encontrado = None
    for p in productos:
        if p.nombre.lower() == nombre_buscado.lower():
            producto_encontrado = p
            break
    if producto_encontrado is None:
        print("Producto no encontrado en el catálogo.")
        return
    cantidad = validar_numero(" Cantidad a vender  : ", int, 1)
    if cantidad > producto_encontrado.stock:
        print(f"Stock insuficiente. Disponible: {producto_encontrado.stock}")
        return
    subtotal = producto_encontrado.precio * cantidad
    producto_encontrado.stock -= cantidad
    ventas.append(Venta(nombre_buscado, cantidad, subtotal))
    print(f"  Venta registrada. Subtotal: S/. {subtotal:.2f}")
    if producto_encontrado.stock <= producto_encontrado.stock_min:
        print(f"  ALERTA: '{producto_encontrado.nombre}' tiene stock bajo ({producto_encontrado.stock} unid.)")

def mostrar_productos():
    print("\n--- Catálogo de Productos ---")
    if not productos:
        print("No hay productos registrados.")
        return
    print(f"  {'NOMBRE':<20} | {'PRECIO':>8} | {'STOCK':>6} | {'MIN':>4} | CATEGORÍA")
    print("  " + "-" * 65)
    for p in productos:
        print(f"  {p.nombre:<20} | S/. {p.precio:>5.2f} | {p.stock:>6} | {p.stock_min:>4} | {p.categoria}")
    print(f"\n Total de productos: {len(productos)}")

def mostrar_alertas():
    print("\n--- Alertas de Stock Bajo ---")
    hay_alertas = False
    for p in productos:
        if p.stock <= p.stock_min:
            print(f"  {p.nombre:<20} — Stock: {p.stock} (mínimo: {p.stock_min})")
            hay_alertas = True
    if not hay_alertas:
        print("Todos los productos tienen stock suficiente.")

def mostrar_reporte():
    print("\n--- Reporte del Día ---")
    if not ventas:
        print(" No se han registrado ventas hoy.")
        return
    total = 0
    for v in ventas:
        print(f"  {v.nombre_producto:<20} x{v.cantidad:>3}  — S/. {v.subtotal:.2f}")
        total += v.subtotal
    print("  " + "-" * 45)
    print(f" Nº de ventas : {len(ventas)}")
    print(f" TOTAL        : S/. {total:.2f}")

def menu_principal():
    opciones = {"1", "2", "3", "4", "5", "6", "7"}
    while True:
        print("\n" + "=" * 40)
        print("  BODEGA 'EL AHORRO' — MENÚ PRINCIPAL")
        print("=" * 40)
        print("  1. Agregar producto")
        print("  2. Registrar venta")
        print("  3. Ver todos los productos")
        print("  4. Ver alertas de stock")
        print("  5. Reporte del día")
        print("  6. Guardar datos")
        print("  7. Salir")
        print("-" * 40)
        opcion = input("  Elija una opción (1-7): ").strip()
        if opcion not in opciones:
            print("  Opción inválida. Ingrese un número del 1 al 7.")
            continue
        if   opcion == "1": agregar_producto()
        elif opcion == "2": registrar_venta()
        elif opcion == "3": mostrar_productos()
        elif opcion == "4": mostrar_alertas()
        elif opcion == "5": mostrar_reporte()
        elif opcion == "6": guardar_datos()
        elif opcion == "7":
            guardar_datos()
            print("\n  ¡Hasta luego!")
            break

if __name__ == "__main__":
    print("  Cargando datos...")
    cargar_datos()
    menu_principal()