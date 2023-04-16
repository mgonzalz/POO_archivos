
def read_csv(filename):
    estudiantes = []
    
    with open(filename,encoding='utf-8-sig') as f: #encoding='utf-8-sig' para que se lea bien el archivo con acentros y ñ
        lineas = f.readlines()  # Descartar la primera línea
    #Apellidos;Nombre;Asistencia;Parcial1;Parcial2;Ordinario1;Ordinario2;Practicas;OrdinarioPracticas
        for linea in lineas[1:]:
            informacion = linea.split(';')
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
    return sorted(estudiantes, key=lambda estudiante: estudiante['Apellidos']) #lambda define el criterio de ordenamiento

def print_students(estudiantes):
    for estudiante in estudiantes:
        print("Nombre completo: {} {}\nAsistencia: {}\nParcial 1: {}\nParcial 2: {}\nOrdinario 1: {}\nOrdinario 2: {}\nPrácticas: {}\nOrdinario de prácticas: {}\n".format(estudiante['Nombre'], estudiante['Apellidos'], estudiante['Asistencia'], estudiante['Parcial1'], estudiante['Parcial2'], estudiante['Ordinario1'], estudiante['Ordinario2'], estudiante['Practicas'], estudiante['OrdinarioPracticas']))

print_students(read_csv('data/calificaciones.csv'))
