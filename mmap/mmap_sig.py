import os, sys
import argparse
import mmap
import signal

parser = argparse.ArgumentParser(description="Reescribir a MAYUSCULAS.")
parser.add_argument('-f', help="Programa crear un segmento de memoria compartida anónima, y genera dos hijos: H1 y H2")
args = parser.parse_args()

area = mmap.mmap(-1, 1024)

def send_to_parent(s, f):
    area.seek(0)
    line = area.readline()
    print("Linea ingresada: ", line.decode())
    os.kill(child2, signal.SIGUSR1)

def mayus(s, f):
    area.seek(0)
    line = area.readline()
    file.write(line.decode().upper())
    file.flush()
    print("Ingrese linea: ")

def end_child2(s, f):
    print("Hijo 2 terminando...")
    os._exit(0)

def end_parent_child2(s, f):
    os.kill(child2, signal.SIGUSR2)
    
def main():
    signal.signal(signal.SIGUSR1, send_to_parent)
    signal.signal(signal.SIGUSR2, end_parent_child2)
    global child1
    child1 = os.fork()
    if child1 == 0:
        print("Ingrese linea: ")
        for line in sys.stdin:
            if line == "bye\n":
                os.kill(os.getppid(), signal.SIGUSR2)
                print("Hijo 1 terminando...")
                os._exit(0)
            area.seek(0)
            area.write(line.encode())
            area.seek(0)
            os.kill(os.getppid(), signal.SIGUSR1) 
    else:
        global child2
        child2 = os.fork()
        if child2 == 0:
            signal.signal(signal.SIGUSR1, mayus)
            signal.signal(signal.SIGUSR2, end_child2)

            while True:
                signal.pause()

        else:
            os.waitpid(child1, 0)
            os.waitpid(child2, 0)
            print("Padre terminando...")

if __name__ == '__main__':
    file = open(args.f, 'a')
    main()