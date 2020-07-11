import logging
import time
import threading

l = logging.getLogger("musu logeris")
h = logging.StreamHandler()
f = logging.Formatter("%(asctime)s: %(message)s")
h.setFormatter(f)
l.addHandler(h)
l.setLevel(logging.INFO)

def pinigu_surinkimo_stotele(Car):
    l.info("processas vygdomas")
    time.sleep(2)
    l.info("processas uzdarytas")

if __name__ == "__main__":
    cars = ["Audi", "BMW", "Toyota"]
    threads = []
    start_time = time.time()

    for car in cars:
       # pinigu_surinkimo_stotele(car)
        new_thread = threading.Thread(target=pinigu_surinkimo_stotele, args=(car,))
        threads.append(new_thread)
        new_thread.start()
    print(new_thread)

    for thread in threads:
        thread.join()
    print(F"proceso laikas: {start_time - time.time()}")