#printinam stringa i terminala
print("hello world!")


# taip sukuraimas exeptionas
raise Exception("syntaxError")

#listo sukurimas
myList = ["pirmas", "antras", "trecias"]

#pasiekti listo antra elementa
print(myList[0])

# funkcijos kurimas
    def random_exeption():
        print("")

#funkcijos kvietimas
    random_exeption()

#for loopas
for i in range(6):
    print(i)

#Dictinary sukurimas
ErrorOc = {
    IndexError : 0,
    SyntaxError : 0
}

#dic key pakeitimas
ErrorOc[IndexError] = 5

#loggerio i konsole sukurimas
import logging

l = logging.getLogger("musu logeris")
h = logging.StreamHandler()
f = logging.Formatter("%(asctime)s: %(message)s")
h.setFormatter(f)
l.addHandler(h)
l.setLevel(logging.INFO)

#loggerio kurimas i faila
import logging
l = logging.getLogger("LOGGERIS i faila.log")
h = logging.FileHandler("failas.log")
f = logging.Formatter("%(asctime)s: [%(levelname)s] %(message)s faile: %(filename)s eiluteje: %(lineno)s")
h.setFormatter(f)
l.setLevel(logging.INFO)
l.addHandler(h)
#cia perduoda i failas.log
l.critical("auksciausias loggas 50")
l.error("error logas 40")
l.warning("warning logas 30")
l.info("info logas 20")
l.debug("debug logas 10")

#class kurimas

class Car:
    model = ""
    price = 0.0
    year = 0

    def __init__(self, model, price, year):
        self.model = model
        self.price = price
        self.year = year
    def __str__(self):
        return (f"{self.brand}: {self.model} year: {self.year} price: {self.price}")

#subclass kurimas
class Audi(Car):
    brand = "Audi"
    def __init__(self, model, price, year):
        super().__init__(model, price, year)

#car =Audi("a6", 1000.00, 1999)
#print(car)

#dekoratoriaus kurimas per class
class HTMLHeader:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        result = self.func(*args, **kwargs)
        return f"<h1>{result}</h1>"


@HTMLHeader
def prepare_title(title_string):
    return title_string.title() # .title() padaro kiekviena zody is didziosios raides


if __name__ == "__main__":
    print(prepare_title("this is a section title!"))

# dekoratorius per classe su functtools
import functools


class Multiply:
    def __init__(self, multiplier):
        self.multiplier = multiplier

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return result * self.multiplier  #is funcijos(double_addition) paimtas atsakymas ir atliekama dekoratoriuje daugyba

        return wrapper


@Multiply(2)
def double_addition(a, b):
    return a + b


@Multiply(3)
def triple_addition(a, b):
    return a + b


if __name__ == "__main__":
    print(double_addition(2, 2))
    print(triple_addition(1, 1))

#pool threading
import concurrent.futures

with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    executor.submit(fn, *args, **kwargs)
#threading Locks
class TollBooth:
    def __init__(self):
        self.register = 0.0
        self.__lock = threading.Lock() #persivadinti

    def process_fee(self, car, fee):
        l.info(f"Processing {car}'s fee. Current total: {self.register}")
        with self.__lock: #context menegeris procese riboja svarbius veiksmus
            new_total = self.register + fee  # Toll booth calculates a new total
            time.sleep(0.1)  # processing takes 0.1 seconds
            self.register = new_total  # New total is saved after 0.1 seconds
        # notice operations outside the critical section are still concurrent
        time.sleep(1)
        l.info(f"Done processing {car}'s fee. New total: {self.register}")

        #poto pool threadas issikviecia Process_fee()

#log level atributes
"""
Attribute name
Format
Description

args
You shouldn’t need to format this yourself.
The tuple of arguments merged into msg to produce message, or a dict whose values are used for the merge (when there is only one argument, and it is a dictionary).

asctime
%(asctime)s
Human-readable time when the LogRecord was created. By default this is of the form ‘2003-07-08 16:49:45,896’ (the numbers after the comma are millisecond portion of the time).

created
%(created)f
Time when the LogRecord was created (as returned by time.time()).

exc_info
You shouldn’t need to format this yourself.
Exception tuple (à la sys.exc_info) or, if no exception has occurred, None.

filename
%(filename)s
Filename portion of pathname.

funcName
%(funcName)s
Name of function containing the logging call.

levelname
%(levelname)s
Text logging level for the message ('DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL').

levelno
%(levelno)s
Numeric logging level for the message (DEBUG, INFO, WARNING, ERROR, CRITICAL).

lineno
%(lineno)d
Source line number where the logging call was issued (if available).

message
%(message)s
The logged message, computed as msg % args. This is set when Formatter.format() is invoked.

module
%(module)s
Module (name portion of filename).

msecs
%(msecs)d
Millisecond portion of the time when the LogRecord was created.

msg
You shouldn’t need to format this yourself.
The format string passed in the original logging call. Merged with args to produce message, or an arbitrary object (see Using arbitrary objects as messages).

name
%(name)s
Name of the logger used to log the call.

pathname
%(pathname)s
Full pathname of the source file where the logging call was issued (if available).

process
%(process)d
Process ID (if available).

processName
%(processName)s
Process name (if available).

relativeCreated
%(relativeCreated)d
Time in milliseconds when the LogRecord was created, relative to the time the logging module was loaded.

stack_info
You shouldn’t need to format this yourself.
Stack frame information (where available) from the bottom of the stack in the current thread, up to and including the stack frame of the logging call which resulted in the creation of this record.

thread
%(thread)d
Thread ID (if available).

threadName
%(threadName)s
Thread name (if available).
"""
