from mensajes.mensaje import mensaje
from mensajes.nodo_mensaje import nodo_mensaje
import re
import json
class lista_mensaje:
    def __init__ (self):
        self.head = None
        self.mensajes_count = 0
    def add_mensaje(self,texto,fecha):
        nodo_temporal = nodo_mensaje(mensaje(texto,fecha))
        if self.head == None:
            self.head = nodo_temporal
            self.mensajes_count += 1
            return
        aux = self.head
        while aux.siguiente:
            aux = aux.siguiente
        aux.siguiente= nodo_temporal
    def recorrer(self):
        aux = self.head
        while aux:
            print("FECHA: ",aux.mensaje.fecha," TEXTO: ",aux.mensaje.texto)
            aux = aux.siguiente

    def devolver_mensaje(self):
        if self.head == None:
            print("Lista vacia")
            return "Lista vacia"
        buffer=""
        aux = self.head
        while aux:
            buffer += "FECHA: "+aux.mensaje.fecha+" TEXTO: "+aux.mensaje.texto+"\n"
            aux = aux.siguiente
        return buffer
    def inicializar(self):
        self.head = None
        self.mensajes_count = 0
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
        menciones=[]
        if self.head == None:
            print("Lista vacia")
            return "Lista vacia"
        aux = self.head
        while aux:
            for palabra in aux.mensaje.texto.split():
                regex = r'^@[a-zA-Z0-9_\-]+$'
                match = re.match(regex, palabra)
                if match:
                    menciones.append(palabra)
            aux = aux.siguiente
        return json.dumps(menciones)
