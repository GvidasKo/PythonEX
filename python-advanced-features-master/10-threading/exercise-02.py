import logging
import time
import threading
import concurrent.futures

l = logging.getLogger("toll_booth")
h = logging.StreamHandler()
f = logging.Formatter("%(asctime)s: %(message)s")
h.setFormatter(f)
l.addHandler(h)
l.setLevel(logging.INFO)


def process_toll_booth_fee(car):
    l.info(f"Processing {car}'s fee...")
    time.sleep(2)  # processing takes 2 seconds
    l.info(f"Done processing {car}'s fee.")


if __name__ == "__main__":
    cars = ["Red", "Blue", "Green"]
    threads = []

    start_time = time.time()
    for car in cars:
        # launch a new thread for each car
        # Daemonic threads won't have time to finish, and they will be
        # killed immidieately after the application finishes.
        new_thread = threading.Thread(
            target=process_toll_booth_fee, args=(car,), daemon=True
        )
        threads.append(new_thread)
        new_thread.start()
    delta_time = time.time() - start_time
    print(f"It took {delta_time:.1f}s to process all the cars.")
