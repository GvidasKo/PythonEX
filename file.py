#printinam stringa i terminala
print("hello")


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

#logging level name
%(levelname)s

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