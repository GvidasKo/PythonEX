import multiprocessing
import logging
import time
import math

l = logging.getLogger("MultiProcessing")
h = logging.StreamHandler()
f = logging.Formatter("%(asctime)s: %(message)s")
h.setFormatter(f)
l.addHandler(h)
l.setLevel(logging.INFO)

def square_root(i):
    for k in range(10000000):
        resulttatas = math.sqrt(i)
    l.info(f"skaiciaus {i} saknis yra {resulttatas}")



if __name__ == "__main__":
    i = 0
    multiprocessing.Queue()
    multiprocessing.Lock()
    procesai = [
        multiprocessing.Process(target=square_root(i + 665007,)) for i in range(7)

    ]
    #start_time = time.time()
    print(F"procesu kiekis: {len(procesai)}")
    for process in procesai:
        process.start()
    for process in procesai:
        process.join()
    print(f"uzduotis uztruko: {stop.time - start_time}")
    #procesai[0].start()