import os, argparse

parser = argparse.ArgumentParser(description="pruebanding")

parser.add_argument('-i', "--source_file", type=str, required=True, help="Nombre de archivo origen")
parser.add_argument('-o', "--destiny_file", type=str, help="Nombre de archivo destino")


args = parser.parse_args()

if os.path.isfile(args.source_file):
    print("El archivo origen existe")
    file = open(args.source_file, 'r')
    cont = file.read()
    file.close()
    file2 = open(args.destiny_file, 'a+')
    file2.write(cont)
    file2.close()
    print("Contenido copiado")
else:
    print("El archivo origen no existe")
