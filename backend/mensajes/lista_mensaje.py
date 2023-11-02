from mensajes.mensaje import mensaje as msj
from mensajes.nodo_mensaje import nodo_mensaje
import re
import json
class lista_mensaje:
    def __init__ (self):
        self.head = None
        self.mensajes_count = 0
        self.mensajes=[]
        self.positivos=[]
        self.negativos=[]
        self.positivos_count=0
        self.negativos_count=0
        self.menciones=[]
    def add_mensaje(self,texto,fecha):
        new_Mensaje = msj(texto,fecha)
        nodo_temporal = nodo_mensaje(new_Mensaje)
        if self.head == None:
            self.head = nodo_temporal
            self.mensajes_count += 1
            self.mensajes.append(new_Mensaje)
            return
        aux = self.head
        while aux.siguiente:
            aux = aux.siguiente
        aux.siguiente= nodo_temporal
        self.mensajes.append(new_Mensaje)
    def add_positivos(self,positivo):
        self.positivos.append(positivo)
        self.positivos_count+=1
    def add_negativos(self,negativo):
        self.negativos.append(negativo)
        self.negativos_count+=1

    def recorrer(self):
        aux = self.head
        while aux:
            print("FECHA: ",aux.mensaje.fecha," TEXTO: ",aux.mensaje.texto)
            aux = aux.siguiente
    def devolver_mensaje(self):
        if self.head == None:
            print("Lista vacia")
            return "Lista vacia"
        return json.dumps([msj.dump() for msj in self.mensajes],indent=4)
    def inicializar(self):
        self.head = None
        self.mensajes_count = 0
        self.mensajes=[]
        self.positivos=[]
        self.negativos=[]
        self.positivos_count=0
        self.negativos_count=0

    def devolver_hashtags(self):
        hashtags=[]
        if self.head == None:
            print("Lista vacia")
            return "Lista vacia"
        aux = self.head
        while aux:
            for palabra in aux.mensaje.texto.split():
                regex = r'^#[a-zA-Z0-9_\-]+\#$'
                match = re.match(regex, palabra)
                if match:
                    hashtags.append(palabra)
            aux = aux.siguiente
        return json.dumps(hashtags)
    def get_menciones(self):
        regex = r'^@[a-zA-Z0-9_\-]+$'
        if self.head == None:
            print("Lista vacia")
            return "Lista vacia"
        aux = self.head
        while aux:
            for palabra in aux.mensaje.texto.split():
                if re.match(regex, palabra):self.menciones.append(palabra)
            aux = aux.siguiente
        return json.dumps(self.menciones)
    def get_sentimientos(self):
        for positivo in self.positivos:
            print(positivo)
        print("Mensaje Positivos: ",self.positivos_count)
        for negativo in self.negativos:
            print(negativo)
        print("Mensaje Negativos: ",self.negativos_count)
    
    def definir_mensaje(self):
        count_positivos=0
        count_negativos=0
        lista_mensajes=[]
        if self.head == None:
            print("Lista vacia")
            return "Lista vacia"
        aux = self.head
        while aux:
            for palabra in aux.mensaje.texto.split():
                if palabra in self.positivos:
                    count_positivos+=1
                if palabra in self.negativos:
                    count_negativos+=1
            if count_positivos>count_negativos: lista_mensajes.append("Positivo")
            elif count_positivos<count_negativos: lista_mensajes.append("Negativo")
            else: lista_mensajes.append("Neutro")
            aux = aux.siguiente
        x=0
        y=0
        z=0
        for mensaje in lista_mensajes:
            if mensaje=="Positivo":x+=1
            elif mensaje=="Negativo":y+=1
            elif mensaje=="Neutro":z+=1
        response={"Mensajes positivos: ":x,"Mensajes negativos: ":y,"Mensajes neutros: ":z,"Total de mensajes: ":x+y+z}
        return response
