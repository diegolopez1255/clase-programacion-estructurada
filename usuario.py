# usuarios/usuario.py
from conexionBD import obtener_conexion
from funciones import limpiar_pantalla, pausar
import hashlib

usuario_actual = None  # Guardar sesión

def menu_inicio_sesion():
    global usuario_actual
    while True:
        limpiar_pantalla()
        print(".:: Cocina Económica ::.")
        print("1.- 📝 Registro")
        print("2.- 🔐 Login")
        print("3.- 🚪 Salir")
        opcion = input("\nElige una opción: ")

        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            if login_usuario():
                menu_usuario()
        elif opcion == "3":
            print("Saliendo del sistema...")
            break
        else:
            print("❌ Opción inválida")
            pausar()

def registrar_usuario():
    limpiar_pantalla()
    print("== 📝 Registro de Usuario ==")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    email = input("Correo electrónico: ")
    password = input("Contraseña: ")
    password_hash = hashlib.sha256(password.encode()).hexdigest()

    try:
        conexion = obtener_conexion()
        if conexion:
            cursor = conexion.cursor()
            cursor.execute("""
                INSERT INTO usuarios (username, email, password)
                VALUES (%s, %s, %s)
            """, (f"{nombre} {apellido}", email, password_hash))
            conexion.commit()
            conexion.close()
            print("✅ Usuario registrado exitosamente.")
        else:
            print("❌ No se pudo conectar a la base de datos.")
    except Exception as e:
        print(f"❌ Error: {e}")
    pausar()

def login_usuario():
    global usuario_actual
    limpiar_pantalla()
    print("== 🔐 Iniciar Sesión ==")
    email = input("Correo electrónico: ")
    password = input("Contraseña: ")
    password_hash = hashlib.sha256(password.encode()).hexdigest()

    try:
        conexion = obtener_conexion()
        if conexion:
            cursor = conexion.cursor()
            cursor.execute("SELECT id_usuario, username FROM usuarios WHERE email = %s AND password = %s", (email, password_hash))
            usuario = cursor.fetchone()
            conexion.close()
            if usuario:
                usuario_actual = {"id": usuario[0], "nombre": usuario[1]}
                print(f"\n✅ Bienvenido, {usuario[1]}!")
                pausar()
                return True
            else:
                print("❌ Credenciales incorrectas")
        else:
            print("❌ Error de conexión.")
    except Exception as e:
        print(f"❌ Error: {e}")
    pausar()
    return False

def menu_usuario():
    from ventas.ventas import registrar_venta
    global usuario_actual
    while True:
        limpiar_pantalla()
        print(f"👤 Usuario: {usuario_actual['nombre']}")
        print("📋 MENÚ PRINCIPAL")
        print("1. ➕ Registrar Producto")
        print("2. 📦 Ver Productos")
        print("3. 🗑️ Borrar Producto")
        print("4. 💲 Actualizar Precio")
        print("5. 📥 Actualizar Stock")
        print("6. 🛒 Registrar Venta")
        print("7. 📈 Ver Ventas")
        print("8. 🚪 Cerrar Sesión")
        opcion = input("\nElige una opción: ")

        if opcion == "1":
            from productos.productos import registrar_producto
            registrar_producto()
        elif opcion == "2":
            from productos.productos import ver_inventario
            ver_inventario()
        elif opcion == "3":
            from productos.productos import eliminar_producto
            eliminar_producto()
        elif opcion == "4":
            from productos.productos import actualizar_precio
            actualizar_precio()
        elif opcion == "5":
            from productos.productos import actualizar_stock
            actualizar_stock()
        elif opcion == "6":
            registrar_venta(usuario_actual["id"])
        elif opcion == "7":
            from ventas.ventas import ver_ventas
            ver_ventas()
        elif opcion == "8":
            print("Cerrando sesión...")
            break
        else:
            print("❌ Opción inválida")
            pausar()
