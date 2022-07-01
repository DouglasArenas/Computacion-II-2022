import argparse, multiprocessing as mp
from math import sqrt, log10
from functools import partial

parser = argparse.ArgumentParser(description="Programa que lee una matriz de un archivo txt y y calcula una funcion dada")
parser.add_argument('-p', type=int, help="Genera una cantidad de procesos según el número ingresado")
parser.add_argument('-f', help="Ruta al archivo")
parser.add_argument('-c', help="Calculo a realizar(raiz, pot, log)")
args = parser.parse_args()

def read_matrix(path):
    file = open(path,'r')
    matrix = file.readlines()
    matrix = [line.split(',') for line in matrix]
    return matrix

def calc(func, matriz):
    matriz_nueva = []
    for fila in matriz:
        nueva_fila = []
        for elemento in fila:
            elemento = function_calculate(func, elemento)
            nueva_fila.append(elemento)
        matriz_nueva.append(nueva_fila)
    print(matriz_nueva)

def log(element):
    return log10(int(element))

def raiz(element):
    return sqrt(int(element))

def pot(element):
    return int(element)**int(element)

def function_calculate(func, element):
    functions = {
        'pot': pot(element),
        'raiz': raiz(element),
        'log': log(element)
    }
    return functions[func]

def main():
    pool = mp.Pool(args.p)
    results = pool.starmap(partial(calc, args.c), [[read_matrix(args.f)]])

if __name__ == '__main__':
    main()