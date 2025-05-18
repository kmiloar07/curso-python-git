import csv

def read_csv(path): #Esta función recibe un parámetro path, que es la ruta del archivo CSV a leer.
    with open(path, 'r') as csvfile: #Se abre el archivo en modo lectura ('r'). La estructura with open(...) se usa para garantizar que el archivo se cierre automáticamente después de usarse
        reader = csv.reader(csvfile, delimiter=',') #Se crea un objeto reader de csv.reader, que interpreta el archivo CSV, usando la coma (',') como separador de columnas.
        header = next(reader) #Se usa next(reader) para obtener la primera fila del archivo, que generalmente contiene los nombres de las columnas (encabezados).
        #PROCESAMIENTO DE DATOS
        data = [] #Se inicializa una lista data para almacenar los datos procesados. 
        for row in reader: #Luego, se recorre cada fila del archivo CSV.
            #CREACIÓN DE UN DICCIONARIO PARA CADA FILA
            iterable = zip(header, row) #Combina cada nombre de columna (de header) con el valor correspondiente de la fila (row).
            country_dict = {key: value for key, value in iterable} #Crea un diccionario donde las claves son los nombres de columna y los valores son los datos de la fila.
            data.append(country_dict) #Se agrega el diccionario creado a la lista data.
        return data

if __name__ == '__main__':
    data = read_csv('./app/data.csv') #Se llama a la función read_csv con la ruta del archivo ./app/data.csv, cargando el contenido en la variable data.
    print(data)