import os, argparse, string, time

parser = argparse.ArgumentParser(description="Programa que genera 'n' procesos hijos y cada hijo está asociado a una letra del abecedario(hasta 26 procesos)")
parser.add_argument('-n', type=int, help="Genera una cantidad de procesos según el número ingresado")
parser.add_argument('-r', type=int, help="Almacena en el archivo su letra según el número ingresado")
parser.add_argument('-f', help="Path del archivo a trabajar")
parser.add_argument('-v', action="store_true", help="Ingresa en modo verboso")

args = parser.parse_args()
abc = list(string.ascii_uppercase)
def child(l):
    if os.fork() == 0:
        if args.v:
                print(f"Proceso {os.getpid()} escribiendo letra '{l}'")
        file.write(l)
        file.flush()
        time.sleep(1)
        os._exit(0)
    
def open_file(path):
    file = open(path, 'w+')
    return file

def read_file(path):
    file = open(path, 'r')
    text = file.readlines()
    print(text) 

if __name__ == "__main__":
    file = open_file(args.f)
    try:
        for i in range(args.n):
            child(abc[i])
    except IndexError:
        print("\nDemasiada cantidad de procesos(máximo 26)\n")
    try:
        for i in range(args.n):
            os.wait()
    except ChildProcessError:
        pass
    read_file(args.f)