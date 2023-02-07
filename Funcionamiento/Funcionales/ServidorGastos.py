from socket import socket
from pathlib import Path
from xlrd import open_workbook
from xlutils.copy import copy
#Ip server-->172.31.30.112

class ServidorGastos ():
      
#Conecta y acepta al cliente
    def conexion(self):
        self.s=socket()  
        # Escuchar peticiones en el puerto 6030.  
        self.s.bind(("localhost", 8080))
        self.s.listen(0)
        print("Escuchando por 8080")
        self.conn, self.addr=self.s.accept()
#Escucha lo que el cliente quiere
#tipo=0-->Introducir datos en excel
#tipo=1-->Descargar el excell
    def escuchaTipo(self):
        self.tipo=self.conn.recv(1024)      
    #Le envía el excell al cliente
    def enviaExcel(self):
        print("Enviando archivo...")
        file_size = Path('recibido.xls').stat().st_size
        while True:
            f=open("recibido.xls","rb")
            print(file_size)
            content=f.read(file_size)
            tam=(str)(file_size)
            while content:
                 #enviar tamaño 
                self.conn.send((bytes)(tam,'ascii'))
                #Enviar archivo
                self.conn.send(content)
                content=f.read(file_size)
                
            break
        #~Se utiliza el 1 para indicar al cliente que ya se ha mandado todo.
        try:
            self.conn.send(chr(1))
        except TypeError:
            self.conn.send(bytes(chr(1), "utf-8"))
        
        #se cierran conexiones
        self.s.close()
        f.close()
        print("El archivo se envió correctamente")
    
#Aquí modificamos el excell con los datos obtenidos.
    def modificaExcell(self):
        
    

#Arranca para empezar a escuchar
    def arranca(self):
        self.conexion()
        self.escuchaTipo()
        if (self.tipo==b'1'):
            self.enviaExcel()
        else:
            print(self.tipo)
            print("Se han recibido los  datos")
#Cierra los sockets 
    def close(self):
        self.conn.close()
        self.s.close()
    
if __name__=="__main__":
    while True:
        server=ServidorGastos()
        server.arranca()
        server.close()
        

    



