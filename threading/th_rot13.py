import threading, sys, os, codecs

def read_sys(w):
    print('Ingrese texto a cifrar: ')
    line = sys.stdin.readline()
    os.write(w, line.encode("ascii"))

def write(r):
    line = os.read(r, 100).decode()
    line_encode = codecs.encode(line, 'rot_13')
    print(f'Texto cifrado: {line_encode}')

if __name__ == '__main__':
    r, w = os.pipe()
    th1 = threading.Thread(target=read_sys, args=(w,))
    th2 = threading.Thread(target=write, args=(r,))
    th1.start()
    th2.start()
    th1.join()
    th2.join()