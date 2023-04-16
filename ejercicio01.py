# FUNCIONES
def nota_en_float(numero_str):
    '''Función para sustituir la coma (,) por un punto (.) y que el número sea de tipo float'''
    if numero_str != '':
        numero_str = numero_str.replace(',', '.') 
        n = float(numero_str)
        return n
    else:
        return ''


def read_csv(filename):
    ''' Función que recibe el fichero de calificaciones y devuelve una lista de diccionarios, 
    donde cada diccionario contiene la información de los exámenes y la asistencia de un alumno. 
    La lista tiene que estar ordenada por apellidos.'''
    lista_estudiantes = []
    
    with open(filename, encoding = 'utf-8-sig') as f: #encoding='utf-8-sig' para que se lea bien el archivo con acentos y ñ
        lineas = f.readlines()  # Descartar la primera línea
    #Apellidos;Nombre;Asistencia;Parcial1;Parcial2;Ordinario1;Ordinario2;Practicas;OrdinarioPracticas
        for linea in lineas[1:]:
            linea =  linea.rstrip('\n')  # quitar la cadena de caracteres '\n' del final de cada línea
            informacion = linea.split(';')  # y dividir la línea del fichero en una lista de strings
            # diccionario con la info del estudiante
            estudiante = {}
            estudiante["Apellidos"] = informacion[0]
            estudiante["Nombre"] = informacion[1]
            estudiante["Asistencia"] = informacion[2]
            estudiante["Parcial1"] = nota_en_float(informacion[3])
            estudiante["Parcial2"] = nota_en_float(informacion[4])
            estudiante["Ordinario1"] = nota_en_float(informacion[5])
            estudiante["Ordinario2"] = nota_en_float(informacion[6])
            estudiante["Practicas"] = nota_en_float(informacion[7])
            estudiante["OrdinarioPracticas"] = nota_en_float(informacion[8])
            # añadimos el diccionario con la info del estudiante a la lista de estudiantes
            lista_estudiantes.append(estudiante) 
    
    return sorted(lista_estudiantes, key = lambda estudiante: estudiante['Apellidos']) #lambda define el criterio de ordenamiento


def print_students(lista_estudiantes):
    '''Función para imprimir la lista de estudiantes'''
    for estudiante in lista_estudiantes:
        print(f"Nombre completo: {estudiante['Nombre']} {estudiante['Apellidos']} \nAsistencia: {estudiante['Asistencia']} \nParcial 1: {estudiante['Parcial1']} \nParcial 2: {estudiante['Parcial2']} \nOrdinario 1: {estudiante['Ordinario1']} \nOrdinario 2: {estudiante['Ordinario2']} \nPrácticas: {estudiante['Practicas']} \nOrdinario Prácticas: {estudiante['OrdinarioPracticas']} \n")



# CÓDIGO EJECUTABLE
if __name__ == '__main__':
    print_students(read_csv('data/calificaciones.csv'))
