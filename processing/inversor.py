import argparse, os

parser = argparse.ArgumentParser(description="Archivo que genera procesos que invierten las lineas de un texto")
parser.add_argument('-f', help="Ruta del archivo a trabajar")
args = parser.parse_args()

file = open(args.f, 'r')
r, w = os.pipe()
rr, ww = os.pipe()
lines = file.readlines()

print(lines)
line = "".join(lines)
print(line)
os.write(w, line.encode())

for i in range(len(lines)):
    if os.fork() == 0:
        os.close(w)
        os.close(rr)
        print("Child reading...")
        r = os.fdopen(r)
        text = r.read()
        print(text)
        print("Child writing...")
        os.write(ww, text)
        print("Child ending...")
        os._exit(0)

for i in range(len(lines)):
    os.wait()
print("father reading")
rr = os.fdopen(rr)
print("Father reading childs... ", rr.read())
