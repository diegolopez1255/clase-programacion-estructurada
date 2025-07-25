#proyecto 3
#crear un proyecto qu e permita Gestionar (Administrar)CAlificaciones colocar un menu de aplicaciones para agregar, mostrar y calcular promedio de las calicidicaciones de los alumnos

#notas:
#1.- Utiliza funciones y mandar llamar desde otro archivo
#2.- Utilizar listas para almacenar el nombre de un alumno y 3 califcaciones


import Calificaciones

def main():
    datos = []
    opcion = True
    while opcion:
        Calificaciones.borrarPantalla()
        opcion= Calificaciones.menu_Principal()
        match opcion:
            case "1":
                Calificaciones.AgregarCalificaciones(datos)
                Calificaciones.esperarTecla()
            case "2":
                Calificaciones.MostrarCalificaciones(datos)
                Calificaciones.esperarTecla()
            case "3":
                Calificaciones.CalcularPromedio(datos)
                Calificaciones.esperarTecla()
            case "4":
                Calificaciones.BuscarAlumno(datos)
                Calificaciones.esperarTecla()    
            case "5":
                opcion = False
                print("\n\tTerminaste la ejecución del programa.")
            case _:
                input("\n\t Opción inválida. Presiona Enter para intentarlo de nuevo.")

if __name__ == "__main__":
    main()