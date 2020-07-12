import multiprocessing
import logging
import time
import math
import random

l = logging.getLogger("MultiProcessing")
h = logging.StreamHandler()
f = logging.Formatter("%(asctime)s: %(message)s")
h.setFormatter(f)
l.addHandler(h)
l.setLevel(logging.INFO)

def generate_random(out_q, n):
    for _ in range(n):
        out_q.put(random.randint(1,985), timeout=1)
        print("ilgis randomo skaiciu querio: ",len(out_q))

def square(in_q, out_q, n):
    for _ in range(n):
        print(f"in_q ilgis yra: {len(in_q)}"
        skaicius = out_q.get(timeout=1)
        in_q.put(skaicius * skaicius, timeout=1)
        print(f"in_q ilgis yra: {len(in_q)}"

def to_bianary(in_q, out_q, n):
    for _ in range(n):
        print(f"in_q ilgis yra: {len(in_q)}"
        skaicius_kvadratu = in_q.get(timeout=1)
        out_q.put(bin(skaicius_kvadratu), timeout=1)
        print(f"in_q ilgis yra: {len(in_q)}"
if __name__ == "__main__":
    queue_a = multiprocessing.Queue(maxsize=1002)
    queue_b = multiprocessing.Queue(maxsize=1002)
    result_q = multiprocessing.Queue(maxsize=1002)

    process_line = [
        multiprocessing.Process(target=generate_random, args=(queue_a, 1000)),
        multiprocessing.Process(target=square, args=(queue_b, 1000)),
        multiprocessing.Process(target=to_bianary, args=(queue_b, result_q, 1000))
    ]

    for i in process_line:
        i.start()
        multiprocessing.Queue.qsize(result_q())
        atsakymai = []

    atsakymai = []
    for i in range(1000):
        print("result q ilgis: ", result_q.qsize())
        atsakymai.append(result_q.get(timeout=2))
    for i in process_line:
        i.join()

    print(len(atsakymai))