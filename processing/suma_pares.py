import os, argparse

parser = argparse.ArgumentParser(description="Suma pares de pids entre 0 y pid del proceso hijo")
parser.add_argument('-n', type=int, help="Genera una cantidad de procesos según el número ingresado")
parser.add_argument('-v', action='store_true',help="Activa el modo verboso")
args = parser.parse_args()


def child():
    if os.fork() == 0:
        if args.v:
            print(f"Starting process {os.getpid()}")
        suma = sum(n for n in range(os.getpid() + 1) if not n & 1)
        print(f"{os.getpid()} - {os.getppid()} : {suma}")
        if args.v:
            print(f"Ending process {os.getpid()}")
        os._exit(0)

for e in range(args.n):
    child()
for e in range(args.n):
    os.wait()
