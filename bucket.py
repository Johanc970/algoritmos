import time
import random

def ordenar_espacios(datos, valores_definidos):
    if len(datos) == 0:
        return datos

    # Crear los buckets (cubetas) basados en los valores definidos
    posiciones = [[] for _ in range(len(valores_definidos) + 1)]

    # Distribuir los elementos en los buckets
    for i in range(len(datos)):
        valor = datos[i]
        for j in range(len(valores_definidos)):
            if valor < valores_definidos[j]:
                posiciones[j].append(valor)
                break
        else:
            posiciones[-1].append(valor)

    # Ordenar cada bucket individualmente y combinar todos los buckets
    vector_ordenado = []
    for posicion in posiciones:
        vector_ordenado.extend(sorted(posicion))

    return vector_ordenado

def funcion_principal():
    # Solicitar al usuario que ingrese el rango y la cantidad de números
    rango_inferior = int(input("Ingresa el límite inferior del rango: "))
    rango_superior = int(input("Ingresa el límite superior del rango: "))
    cantidad_numeros = int(input("Ingresa la cantidad de números aleatorios a generar: "))

    # Generar la lista de números aleatorios
    intervalos = [random.randint(rango_inferior, rango_superior) for _ in range(cantidad_numeros)]
    
    # Calcular automáticamente la cantidad de buckets en función del rango y la cantidad de números
    num_buckets = max(1, cantidad_numeros // 10)  # Aproximadamente un bucket por cada 10 números
    intervalo_buckets = (rango_superior - rango_inferior) // num_buckets
    valores_definidos = [rango_inferior + intervalo_buckets * i for i in range(1, num_buckets)]

    print(f"Lista original: {intervalos}")

    comenzar_tiempo = time.time()

    # Ordenar la lista utilizando el algoritmo Bucket Sort con los valores definidos
    intervalos_ordenados = ordenar_espacios(intervalos, valores_definidos)

    fin_tiempo = time.time()

    print(f"Lista ordenada: {intervalos_ordenados}")
    print(f"Tiempo de ejecución: {fin_tiempo - comenzar_tiempo:.6f} segundos")

if __name__ == "__main__":
    funcion_principal()
