import os, argparse

parse = argparse.ArgumentParser()

parse.add_argument('-i', "--source_file", type=str, help="Nombre de archivo origen")
parse.add_argument('-o', "--destiny_file", type=str, help="Nombre de archivo destino")


args = parser.parse_args()

if os.path.isfile(arg.source_file):
    print("El archivo origen existe")
    file = open(source_file, 'r')
    cont = file.read()
    file.close()
    file2 = open(destiny_file, 'a+')
    file2.write(cont)
    file2.close()

