from socket import socket
from pathlib import Path
def main():
    s=socket()
    s.connect(("50.17.81.243",8080))

    print("Conexion con puerto 22")
    file_size = Path(r'example.xls').stat().st_size
    while True:
        f=open("example.xls","rb")
        tam=(str)(file_size)
        print(tam)
        print(file_size)
        content=f.read(file_size)
    
        while content:
            #enviar tamaño 
            s.send((bytes)(tam,'ascii'))
            #Enviar archivo
            s.send(content)
            content=f.read(file_size)
            
        break
    #~Se utiliza el 1 para inidicar al cliente que ya se ha mandado todo.
    try:
        s.send(chr(1))
    except TypeError:
        s.send(bytes(chr(1), "utf-8"))
    
    #se cierran conexiones
    s.close()
    f.close()
    print("El archivo se envió correnctamente")


if __name__ == "__main__":
    main()

