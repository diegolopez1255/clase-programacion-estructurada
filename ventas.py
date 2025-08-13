# ventas/ventas.py
from conexionBD import obtener_conexion
from funciones import limpiar_pantalla, pausar
from productos.productos import ver_inventario

def registrar_venta(id_vendedor):
    ver_inventario()
    limpiar_pantalla()
    print("== 🛒 Registrar Venta ==")
    
    # Mostrar inventario antes de elegir
    print("\n📦 Productos disponibles:\n")
    try:
        conexion = obtener_conexion()
        if conexion:
            cursor = conexion.cursor()
            cursor.execute("SELECT id_producto, nombre, precio, stock FROM productos WHERE stock > 0")
            productos = cursor.fetchall()
            for p in productos:
                print(f"ID: {p[0]} | {p[1]} | 💲{p[2]} | Stock: {p[3]}")
    except Exception as e:
        print(f"❌ Error: {e}")
        pausar()
        return

    # Pedir producto y cantidad
    id_producto = int(input("\nID del producto: "))
    cantidad = int(input("Cantidad: "))

    try:
        if conexion:
            cursor.execute("SELECT precio, stock FROM productos WHERE id_producto = %s", (id_producto,))
            datos = cursor.fetchone()
            if not datos:
                print("❌ Producto no encontrado.")
                pausar()
                return
            
            precio, stock = datos
            if cantidad > stock:
                print("❌ Stock insuficiente.")
                pausar()
                return

            total = precio * cantidad

            # Registrar la venta
            cursor.execute("""
                INSERT INTO ventas (id_producto, id_usuario, cantidad, total)
                VALUES (%s, %s, %s, %s)
            """, (id_producto, id_vendedor, cantidad, total))

            # Actualizar stock
            cursor.execute("UPDATE productos SET stock = stock - %s WHERE id_producto = %s", (cantidad, id_producto))

            conexion.commit()
            conexion.close()
            print(f"✅ Venta registrada. Total: 💲{total}")
    except Exception as e:
        print(f"❌ Error: {e}")
    pausar()

def ver_ventas():
    limpiar_pantalla()
    print("== 📈 Ventas ==")
    try:
        conexion = obtener_conexion()
        if conexion:
            cursor = conexion.cursor()
            cursor.execute("""
                SELECT v.id_venta, p.nombre, u.username, v.cantidad, v.total
                FROM ventas v
                JOIN productos p ON v.id_producto = p.id_producto
                JOIN usuarios u ON v.id_usuario = u.id_usuario
            """)
            ventas = cursor.fetchall()
            for v in ventas:
                print(f"ID Venta: {v[0]} | Producto: {v[1]} | Vendedor: {v[2]} | Cantidad: {v[3]} | Total: 💲{v[4]}")
            conexion.close()
    except Exception as e:
        print(f"❌ Error: {e}")
    pausar()
