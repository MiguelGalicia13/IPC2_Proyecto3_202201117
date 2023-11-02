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
        #Genera un formato JSON para los mensajes
        return json.dumps([msj.dump() for msj in self.mensajes],indent=4)
    
    def inicializar(self):
        #Reinicia el sistema
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
            for palabra in aux.mensaje.texto.split(): #Recorre cada palabra del mensaje
                regex = r'^#[a-zA-Z0-9_\-]+\#$' #Expresión regular para hashtags
                match = re.match(regex, palabra)
                if match:
                    hashtags.append(palabra) #Si la palabra es un hashtag, lo agrega a la lista
            aux = aux.siguiente
        return json.dumps(hashtags) #Devuelve la lista de hashtags en formato JSON
    def get_menciones(self):
        regex = r'^@[a-zA-Z0-9_\-]+$' #Expresión regular para menciones
        if self.head == None:
            print("Lista vacia")
            return "Lista vacia"
        aux = self.head
        while aux:
            for palabra in aux.mensaje.texto.split():
                if re.match(regex, palabra):self.menciones.append(palabra) #Si la palabra es una mención, la agrega a la lista
            aux = aux.siguiente
        return json.dumps(self.menciones) #Devuelve la lista de menciones en formato JSON
    def get_sentimientos(self):
        for positivo in self.positivos:
            print(positivo)
        print("Mensaje Positivos: ",self.positivos_count)
        for negativo in self.negativos:
            print(negativo)
        print("Mensaje Negativos: ",self.negativos_count)
    
    def definir_mensaje(self):
        #Genera contadores de los mensajes para cada tipo de mensajes
        count_positivos=0
        count_negativos=0
        lista_mensajes=[]
        if self.head == None:
            print("Lista vacia")
            return "Lista vacia"
        aux = self.head
        while aux:
            for palabra in aux.mensaje.texto.split(): #Recorre cada palabra del mensaje
                if palabra in self.positivos: #Si la palabra está en la lista de positivos, aumenta el contador de positivos
                    count_positivos+=1
                if palabra in self.negativos: #Si la palabra está en la lista de negativos, aumenta el contador de negativos
                    count_negativos+=1
            if count_positivos>count_negativos: lista_mensajes.append("Positivo") #Si el contador de positivos es mayor al de negativos, el mensaje es positivo
            elif count_positivos<count_negativos: lista_mensajes.append("Negativo") #Si el contador de negativos es mayor al de positivos, el mensaje es negativo
            else: lista_mensajes.append("Neutro") #Si los contadores son iguales, el mensaje es neutro
            aux = aux.siguiente
        x=0
        y=0
        z=0
        for mensaje in lista_mensajes: #Cuenta cuántos mensajes hay de cada tipo
            if mensaje=="Positivo":x+=1 #Si el mensaje es positivo, aumenta el contador de positivos
            elif mensaje=="Negativo":y+=1 #Si el mensaje es negativo, aumenta el contador de negativos
            elif mensaje=="Neutro":z+=1 #Si el mensaje es neutro, aumenta el contador de neutros
        response={"Mensajes positivos: ":x,"Mensajes negativos: ":y,"Mensajes neutros: ":z,"Total de mensajes: ":x+y+z}
        return response
