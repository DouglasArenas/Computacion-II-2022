import codecs, sys, multiprocessing as mp

def read(process, queue):
    sys.stdin = open(0)
    line = sys.stdin.readline()
    process.send(line)
    line_queue = queue.get()
    print(line_queue)

def encripter(process, queue):
    line = process.recv()
    encripted_line = codecs.encode(line, "rot_13")
    queue.put(encripted_line)
    
if __name__ == '__main__':
    queue = mp.Queue()
    r, w = mp.Pipe()
    process1 = mp.Process(target=read, args=(r, queue))
    process2 = mp.Process(target=encripter, args=(w, queue))
    process1.start()
    process2.start()
    process1.join()
    process2.join()