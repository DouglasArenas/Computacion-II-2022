import os, argparse, string

parser = argparse.ArgumentParser(description="Programa que genera 'n' procesos hijos y cada hijo està acosiado a una letra del alfabeto")
parser.add_argument('-n', type=int, help="Genera una cantidad de procesos segùn el nùmero ingresado")
parser.add_argument('-r', type=int, help="Almacena en el archivo su letra segùn el nùmero ingresado")
parser.add_argument('-f', help="Path del archivo a trabajar")
parser.add_argument('-v', action="store_true", help="Ingresa en modo verboso")

args = parser.parse_args()

abc = list(string.ascii_uppercase)
f = open(args.f, 'w+')
counter = 0

def child():
    if os.fork() == 0:
        
        if args.v:
                print(f"Proceso {os.getpid()} escribiendo letra '{l}'")
        print(f"Letra")
    os._exit(0)
    
    pass

if __name__ == "__main__":
    for i in range(args.n):
        child()
    for i in range(args.n):
       # os.wait()
        pass
