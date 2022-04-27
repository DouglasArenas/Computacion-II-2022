import argparse, os

parser = argparse.ArgumentParser(description="Archivo que genera procesos que invierten las lineas de un texto")
parser.add_argument('-f', help="Ruta del archivo a trabajar")
args = parser.parse_args()

r, w = os.pipe()
r2, w2 = os.pipe()

def child(n, l):
    for i in range(n):
        if os.fork() == 0:
            print("Hijo escribiendo")
            os._exit(0)

def parent(r):
    r = os.fdopen(r)
    print("Padre leyendo")
    line = r.readline()
    return str(line)
if __name__ == '__main__':
    fd = open(args.f, 'r')
    lines = len(fd.readlines())
    fd.close()
    line = parent(r)
    child(lines, line)
    for i in range(lines):
        os.wait()

