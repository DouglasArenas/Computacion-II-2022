import argparse, os

parser = argparse.ArgumentParser(description="Archivo que genera procesos que invierten las lineas de un texto")
parser.add_argument('-f', help="Ruta del archivo a trabajar")
args = parser.parse_argument()

file = open(args.f, 'r')
r, w = os.pipe()
r2, w2 = os.pipe()

for i in range(len(file.lines())):
    if os.fork() == 0:
        w = os.fdopen(w)
