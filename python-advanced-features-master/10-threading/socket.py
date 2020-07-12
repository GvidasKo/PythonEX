###socket###
###server###
###client###
import socket
import sys
import logging
import threading

l = logging.getLogger("Serverine")
h = logging.StreamHandler()
f = logging.Formatter("%(asctime)s: %(levelname)s!!! %(message)s")
h.setFormatter(f)
l.addHandler(h)
l.setLevel(logging.INFO)

def server(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    except socket.error:
        l.critical("Ivyko kritine klaida (CRITICAL)")
        sys.exit(1)
    sock.bind(("0.0.0.0", port))
    sock.listen(1)
    l.info("Serveris activus")
    conection, _ = sock.accept()
    for _ in range(3):
        data = conection.recv(1024)
        conection.sendall(f"Serverio data: {data.decode()}".encode())
    conection.close()
    sock.close()
    l.info("Closed conection")

def client(sent_to_port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    except socket.error:
        l.critical("Ivyko kritine klaida(CRITICAL)")
        sys.exit(1)
    sock.connect(("localhost", sent_to_port))
    for _ in range(3):
        sock.sendall(input("Zinute").encode())
        print(sock.recv(1024).decode())
    sock.close()
    l.info("Close client")

if __name__ == "__main__":
    port = 8081
    serv = threading.Thread(target=server, args=(port,))
    serv.start()
    client(port)
    serv.join()