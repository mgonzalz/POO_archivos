# IMPORTACIONES
from ejercicio01 import read_csv

# FUNCIONES
def casuistica_examenes(parcial2, ordinario2, practicas, ordinario_practicas):
    '''Función que modeliza los posibles cassos tras realizar el primer parcial.'''
    if parcial2 < 5: # y ha supendido el segundo
        nota2 = ordinario2
        if practicas < 5: # y ha suspendido las prácticas
            nota_practicas = ordinario_practicas
        else: # ha aprobado prcticas
            nota_practicas = practicas
    else: # ha aprobado el segundo parcial
        nota2 = parcial2
        if practicas < 5: # y ha suspendido las prácticas
            nota_practicas = ordinario_practicas
        else: # ha aprobado practicas
            nota_practicas = practicas
    
    return nota2, nota_practicas


def add_final_grade(lista_estudiantes):
    '''Función que añade la nota final a cada estudiante: NF = 0.3*NP1 + 0.3*NP2 + 0.4*NPr'''

    for estudiante in lista_estudiantes:  # para cada diccionario con la info de un estudiante
        # VARIABLES QUE VAMOS A USAR
        parcial1 = estudiante["Parcial1"]
        parcial2 = estudiante["Parcial2"]
        if estudiante["Ordinario1"] != '':
            ordinario1 = estudiante["Ordinario1"]
        else:
            ordinario1 = 0
        if estudiante["Ordinario2"] != '':  
            ordinario2 = estudiante["Ordinario2"]
        else:
            ordinario2 = 0
        if estudiante["Practicas"] != '':
            practicas = estudiante["Practicas"]
        else:
            practicas = 0
        if estudiante["OrdinarioPracticas"] != '':
            ordinario_practicas = estudiante["OrdinarioPracticas"]
        else:
            ordinario_practicas = 0
        
        media_parciales = (estudiante["Parcial1"] + estudiante["Parcial2"])/2
        
        # CASUÍSTICA
        if media_parciales >= 5:  # ha aprobado los parciales
            if practicas >= 5:  # ha aprobado las prácticas
                nota1 = parcial1
                nota2 = parcial2
                nota_practicas = practicas
            
            else: # no ha aprobado las prácticas
                # se presenta a OrdinariaPracticas
                nota1 = parcial1
                nota2 = parcial2
                nota_practicas = ordinario_practicas
        
        else: # ha suspendido algún parcial
            if parcial1 < 5: # ha suspendido el primer parcial
                nota1 = ordinario1
                nota2 = casuistica_examenes(parcial2, ordinario2, practicas, ordinario_practicas)[0]
                nota_practicas = casuistica_examenes(parcial2, ordinario2, practicas, ordinario_practicas)[1]


            else: # ha aprobado el primer parcial
                nota1 = parcial1
                nota2 = casuistica_examenes(parcial2, ordinario2, practicas, ordinario_practicas)[0]
                nota_practicas = casuistica_examenes(parcial2, ordinario2, practicas, ordinario_practicas)[1]


        estudiante['NotaFinal'] = 0.3*nota1 + 0.3*nota2 + 0.4*nota_practicas

    return lista_estudiantes


def print_students_nf(lista_estudiantes):
    '''Función para imprimir la lista de estudiantes (mod. NotaFinal)'''
    for estudiante in lista_estudiantes:
        print(f"Nombre completo: {estudiante['Nombre']} {estudiante['Apellidos']} \nAsistencia: {estudiante['Asistencia']} \nParcial 1: {estudiante['Parcial1']} \nParcial 2: {estudiante['Parcial2']} \nOrdinario 1: {estudiante['Ordinario1']} \nOrdinario 2: {estudiante['Ordinario2']} \nPrácticas: {estudiante['Practicas']} \nOrdinario Prácticas: {estudiante['OrdinarioPracticas']} \nNota Final: {estudiante['NotaFinal']} \n")


# CÓDIGO EJECUTABLE
if __name__ == "__main__":
    print_students_nf(add_final_grade(read_csv('data/calificaciones.csv')))
