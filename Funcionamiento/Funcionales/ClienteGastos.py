from socket import socket,error
#Ip Servidor-->50.17.81.243
s=socket()
tipo='1'
def conexion():
 s.connect(("localhost",8080))
 print("Conexion con puerto 8080")

def enviaTipo():
    s.send((bytes)(tipo,'ascii'))

def recibirExcel():

    f = open("recibido2.xls", "wb")
    
    fileSize=s.recv(1024)    
    print(fileSize)
    print("Leyendo archivo...")
    while True:
        try:
            # Recibir datos del cliente.
            input_data = s.recv((int)(fileSize))
        except error:
            print("Error de lectura.")
            break
        else:
            if input_data:
                # Compatibilidad con Python 3. 
                if isinstance(input_data, bytes):
                    end = input_data[0] == 1
                else:
                    end = input_data == chr(1)
                if not end:
                    # Almacenar datos.
                    f.write(input_data)
                else:
                    break

    print("El archivo se ha recibido correctamente.")
    f.close()


conexion()
enviaTipo()
recibirExcel()