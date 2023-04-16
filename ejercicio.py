import pprint

def read_csv(filename):
    estudiantes = []
    
    with open(filename,encoding='utf-8-sig') as f: #encoding='utf-8-sig' para que se lea bien el archivo con acentros y ñ
        next(f)  # Descartar la primera línea
    #Apellidos;Nombre;Asistencia;Parcial1;Parcial2;Ordinario1;Ordinario2;Practicas;OrdinarioPracticas
        for linea in f:
            informacion = f.readline().split(';')
            estudiante = {}
            estudiante["Apellidos"] = informacion[0]
            estudiante["Nombre"] = informacion[1]
            estudiante["Asistencia"] = informacion[2]
            estudiante["Parcial1"] = informacion[3]
            estudiante["Parcial2"] = informacion[4]
            estudiante["Ordinario1"] = informacion[5]
            estudiante["Ordinario2"] = informacion[6]
            estudiante["Practicas"] = informacion[7]
            estudiante["OrdinarioPracticas"] = informacion[8]
            estudiantes.append(estudiante)
    return sorted(estudiantes, key=lambda estudiante: estudiante['Apellidos'])



def print_students(calificaciones):
    for estudiante in calificaciones:
        print("Nombre completo: {} {}\n".format(estudiante['Nombre'], estudiante['Apellidos']))

print_students(read_csv('calificaciones.csv'))
