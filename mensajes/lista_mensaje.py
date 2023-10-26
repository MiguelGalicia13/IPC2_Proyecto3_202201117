from mensajes.mensaje import mensaje
from mensajes.nodo_mensaje import nodo_mensaje

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
        buffer=""
        aux = self.head
        while aux:
            buffer += "FECHA: "+aux.mensaje.fecha+" TEXTO: "+aux.mensaje.texto+"\n"
            aux = aux.siguiente
        return buffer
    def inicializar(self):
        self.head = None
        self.mensajes_count = 0