
Calificaciones=[]
Calificaciones={}
def borrarPantalla():
    import os
    os.system("cls")

def esperarTecla():
    input("Oprima culaquier tecla para continuar ...")   

     
def AgregarCalificaciones(lista):
  borrarPantalla()
  print("`\U0001F4DD`Agregar Calificaciones")
  nombre = input("`\U0001F464`Nombre del alumno: ").upper().strip()
  calificaciones = []
  for i in range(1,4):
    continua=True
    while continua:
      try:
        cal=float(input(f"`\U0001F4DD`Clificacion:{i}  "))
        if cal >= 0 and cal< 11:
            calificaciones.append(cal)
            continua=False
        else:
            print("`\U0001F4DD`Ingresa un numero valido")
      except ValueError:
        print("| `\u26A0`Ingresa un valor numerico")
  lista.append([nombre]+calificaciones)
  print("| `\u2705`Accion realizada con exito ")

 
def MostrarCalificaciones (lista):
     borrarPantalla()
     print("`\U0001F50D`Mostrar Calificaciones")
     if len(lista)>0:
      print(f"`\U0001F464`Nombre -- Calificaciones")
     for fila in lista:
      print(f"{fila[0]}   -- {fila[1]} -- {fila[2]} -- {fila[3]}")
   
     else:
      print(" `\u26A0`No hay calificaciones registradas en el sistema  `\u274C` ")

def CalcularPromedio(lista):
    borrarPantalla()
    print("===`\U0001F464` Promedios por Alumno `\U0001F464` ===")
    if len(lista) > 0:
        print("`\U0001F464`Nombre -- Promedio")
        for fila in lista:
            promedio = sum(fila[1:]) / 3
            print(f"{fila[0]} -- {promedio:.2f}")
    else:
        print(" `\u26A0` No hay calificaciones registradas.  `\u274C`")

def menu_Principal():
           print("\n\t\t\t..:::  `\U0001F552`Sistema de Gestión de Calificaciones :::...\n 1.\u0031\uFE0F\u20E3- Agregar  \n 2.\u0032\uFE0F\u20E3- Mostrar \n 3.\u0033\uFE0F\u20E3- Calcular Promedio \n 4.\u0034\uFE0F\u20E3- Buscar Alumn0 \n 5.\u0035\uFE0F\u20E3- SALIR ")
           opcion = input("\t Elige una opción: ").strip()
           return opcion

def BuscarAlumno(lista):
    borrarPantalla()
    print("🔎 Buscar Alumno")
    if len(lista) > 0:
        nombre = input("`\U0001F464`Ingrese el nombre del alumno a buscar: ").upper().strip()
        encontrado = False
        for fila in lista:
            if fila[0] == nombre:
                print(f"\n`\U0001F464`Alumno: {fila[0]}")
                print(f"`\U0001F4DD`Calificaciones: {fila[1]}, {fila[2]}, {fila[3]}")
                promedio = sum(fila[1:]) / 3
                print(f"`\U0001F4DD`Promedio: {promedio:.2f}`\U0001F4DD`")
                encontrado = True
                break
        if not encontrado:
            print("`\u26A0`  Alumno no encontrado.`\u26A0` ")
    else:
        print("`\u26A0`  No hay calificaciones registradas.`\u26A0` ")
    esperarTecla()
           
