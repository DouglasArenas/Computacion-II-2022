import os, argparse

parser = argparse.ArgumentParser(description="Programa que lee una matriz de un archivo txt y y calcula una funcion dada")
parser.add_argument('-p', type=int, help="Genera una cantidad de procesos según el número ingresado")
parser.add_argument('-f', help="Ruta al archivo")
parser.add_argument('-c', help="Calculo a realizar(raiz, pot, log)")
args = parser.parse_args()

