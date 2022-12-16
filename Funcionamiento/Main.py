from ServidorGastos import *

class Arranca():
    while True:
        server=ServidorGastos()
        server.arranca()
        server.close()

    


