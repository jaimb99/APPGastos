from socket import socket, error


def main():
    s = socket()

    # Escuchar peticiones en el puerto 6030.
    s.bind(("localhost", 6030))
    s.listen(0)
    print("Escuhando por 6030")
    conn, addr = s.accept()
    
    f = open("recibido.xls", "wb")
    fileSize=conn.recv(1024)
    print("Leyendo archivo...")
    while True:
        try:
            # Recibir datos del cliente.
            
            input_data = conn.recv((int)(fileSize))
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


if __name__ == "__main__":
    main()