import logging
import time
import threading
import concurrent.futures

l = logging.getLogger("musu logeris")
h = logging.StreamHandler()  # nurodo koki mes stringa kursim i kur
f = logging.Formatter("%(asctime)s: %(message)s")  # kaip mes norim suformuoti logeri, ka matyti kaip matyti
h.setFormatter(f)
l.addHandler(h)
l.setLevel(logging.INFO)  # nustatomas logerio levelis


class Stotele:
    def __init__(self):
        self.register = 0.0
        self.__lock = threading.Lock()

    def pinigu_surinkimo_stotele(self, car):
         with self.__lock:
            l.info(f"procesas vygdomas {car}")
            new_total = self.register + fee
            time.sleep(0.1)
             self.register = new_total
            l.info(f"procesas baigtas {car} nauja suma: {self.register}")


if __name__ == "__main__":
    cars = ["audi", "bmw", "opel"]
    threads = []

    start_time = time.time()

    pirma_stotele = Stotele()
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as threder:
        for i in cars:
            threder.submit(pirma_stotele.pinigu_surinkimo_stotele, i, 10.0)
            # threder.submit(Stotele().pinigu_surinkimo_stotele, i, 10.0)
        # threder.map(pinigu_surinkimo_stotele, cars)
    print(f"praleistas laikas: {start_time - time.time()}")