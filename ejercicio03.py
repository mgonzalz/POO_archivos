from ejercicio02 import add_final_grade
from ejercicio01 import read_csv
'''
Una función que reciba una lista de diccionarios como la que devuelve la función anterior y devuelva dos listas, una con los alumnos aprobados y otra con los alumnos suspensos. Para aprobar el curso, la asistencia tiene que ser mayor o igual que el 75%, la nota de los exámenes parciales y de prácticas mayor o igual que 4 y la nota final mayor o igual que 5.
'''
def arreglo(porcentaje): #ARREGLO PORCENTAJE
    if porcentaje != '':
        porcentaje = porcentaje.replace('%', '')
        n = int(porcentaje)
        return n
    else:
        return ' '

def arreglos_vacio(vacio):
    if vacio == '':
        return 0
    else:
        return vacio

def aprobados_suspensos(lista_estudiantes):
    aprobados = []
    suspensos = []
    for estudiante in lista_estudiantes:
        estudiante["Parcial1"] = arreglos_vacio(estudiante["Parcial1"])
        estudiante["Parcial2"] = arreglos_vacio(estudiante["Parcial2"])
        estudiante["Practicas"] = arreglos_vacio(estudiante["Practicas"])
        estudiante["NotaFinal"] = arreglos_vacio(estudiante["NotaFinal"])
        estudiante["Asistencia"] = arreglo(estudiante["Asistencia"])
    for estudiante in lista_estudiantes:
        if estudiante["Asistencia"] >= 75 and estudiante["Parcial1"] >= 4.00 and estudiante["Parcial2"] >= 4.00 and estudiante["Practicas"] >= 4.00 and estudiante["NotaFinal"] >= 5.00:
                aprobados.append(estudiante)
        else:
            suspensos.append(estudiante)
    return aprobados, suspensos

def main():
    lista_estudiantes = add_final_grade(read_csv("data/calificaciones.csv"))
    aprobados, suspensos = aprobados_suspensos(lista_estudiantes)
    print("APROBADOS")
    for estudiante in aprobados:
        print(f"Nombre completo: {estudiante['Nombre']} {estudiante['Apellidos']}")
    print("SUSPENSOS")
    for estudiante in suspensos:
        print(f"Nombre completo: {estudiante['Nombre']} {estudiante['Apellidos']}")

main()
