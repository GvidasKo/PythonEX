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
