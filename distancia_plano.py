#Calcular la distancia entre dos puntos en el plano con coordenadas x e y.
import math

def dist_between_points(x1, y1, x2, y2):
    #Calculo de la distancia
    d = math.sqrt(math.pow(x2-x1, 2) + math.pow(y2-y1, 2))
    print('La distancia entre los puntos en el plano con coordenadas x e y es:', d)
    
#Funcion para validar con un bucle
def obtener_coords(mensaje):
    while True:
        try:
            value = float(input(mensaje))
            return value
        except ValueError:
            print('Error: Por favor, ingrese valores numericos validos')

#Ingreso de datos
print('Ingrese las coordenadas de los puntos x e y')
x1 = obtener_coords('Ingrese la coordenada x del primer punto: ')
y1 = obtener_coords('Ingrese la coordenada y del primer punto: ')
x2 = obtener_coords('Ingrese la coordenada x del segundo punto: ')
y2 = obtener_coords('Ingrese la coordenada y del segundo punto: ')

#Llamada a la función
dist_between_points(x1, y1, x2, y2)

    

