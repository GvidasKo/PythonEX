import threading
import logging
import time
import concurrent.futures
import queue

l = logging.getLogger("Kepykla")
h = logging.StreamHandler()
f = logging.Formatter("%(asctime)s: %(levelname)s!!! %(message)s")
h.setFormatter(f)
l.addHandler(h)
l.setLevel(logging.INFO)

class Kepykla:
    def __init__(self):
        self.storage = storage
        self.__lock = threading.Lock()

    def kepejas(self):
        for i in range(10):
            with self.__lock:
                laikinas_storige = self.storage
                l.info(f"kepam {i}")
                time.sleep(0.1)
                self.storage = laikinas_storige + 1
            l.info(f"Kepykloje yra {self.storage}")
            time.sleep(1)

    def pirkejas(self):
        for i in range(10):
            with self.__lock:
                laikinasis_storige = self.storage
                if laikinasis_storige >= 2:
                    l.info("Turime Pirkeja...")
                    time.sleep(0.2)
                    self.storage = laikinasis_storige - 2
                    l.info(f"Kepykloje liko {self.storage}")
            time.sleep(1)

if __name__ == "__main__":
    kepykla = Kepykla()
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        executor.submit(kepykla.pirkejas)
        executor.submit(kepykla.pirkejas)
        executor.submit(kepykla.kepejas)

