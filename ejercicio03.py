#IMPORTACIONES
from ejercicio02 import add_final_grade
from ejercicio01 import read_csv

#FUNCIONES
def arreglo_porcentajes(porcentaje): #ARREGLO PORCENTAJE
    if porcentaje != '':
        porcentaje = porcentaje.replace('%', '')
        n = int(porcentaje)
        return n
    else:
        return ' '

def arreglos_vacio(vacio): #ARREGLO VACIO
    if vacio == '':
        return 0
    else:
        return vacio

def cambios_lista_estudiantes(lista_estudiantes):
    for estudiante in lista_estudiantes: #PONER 0 EN LOS ESPACIOS VACIOS
        estudiante["Parcial1"] = arreglos_vacio(estudiante["Parcial1"])
        estudiante["Parcial2"] = arreglos_vacio(estudiante["Parcial2"])
        estudiante["Practicas"] = arreglos_vacio(estudiante["Practicas"])
        estudiante["NotaFinal"] = arreglos_vacio(estudiante["NotaFinal"])
        estudiante["Asistencia"] = arreglo_porcentajes(estudiante["Asistencia"])
    return lista_estudiantes

def aprobados_suspensos(lista_estudiantes):
    aprobados = []
    suspensos = []
    for estudiante in lista_estudiantes:
        if estudiante["Asistencia"] >= 75 and estudiante["Parcial1"] >= 4.00 and estudiante["Parcial2"] >= 4.00 and estudiante["Practicas"] >= 4.00 and estudiante["NotaFinal"] >= 5.00:
                aprobados.append(estudiante)
        else:
            suspensos.append(estudiante)
    return aprobados, suspensos

def print_aprobados_suspensos(aprobados, suspensos):
    print("-------------------------APROBADOS-------------------------")
    for estudiante in aprobados:
        print(f"Nombre completo: {estudiante['Nombre']} {estudiante['Apellidos']} \nAsistencia: {estudiante['Asistencia']} \nParcial 1: {estudiante['Parcial1']} \nParcial 2: {estudiante['Parcial2']} \nOrdinario 1: {estudiante['Ordinario1']} \nOrdinario 2: {estudiante['Ordinario2']} \nPrácticas: {estudiante['Practicas']} \nOrdinario Prácticas: {estudiante['OrdinarioPracticas']} \nNota Final: {estudiante['NotaFinal']} \n")    
    print("-------------------------SUSPENSOS-------------------------")
    for estudiante in suspensos:
        print(f"Nombre completo: {estudiante['Nombre']} {estudiante['Apellidos']} \nAsistencia: {estudiante['Asistencia']} \nParcial 1: {estudiante['Parcial1']} \nParcial 2: {estudiante['Parcial2']} \nOrdinario 1: {estudiante['Ordinario1']} \nOrdinario 2: {estudiante['Ordinario2']} \nPrácticas: {estudiante['Practicas']} \nOrdinario Prácticas: {estudiante['OrdinarioPracticas']} \nNota Final: {estudiante['NotaFinal']} \n")

#CÓDIGO EJECUTABLE
if __name__ == "__main__":
    lista_estudiantes = cambios_lista_estudiantes(add_final_grade(read_csv("data/calificaciones.csv")))
    aprobados, suspensos = aprobados_suspensos(lista_estudiantes)
    print_aprobados_suspensos(aprobados, suspensos)
