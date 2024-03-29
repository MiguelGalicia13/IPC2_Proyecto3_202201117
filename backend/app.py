from flask import Flask, jsonify, request
from flask_cors import CORS
import xml.etree.ElementTree as ET
from mensajes.lista_mensaje import lista_mensaje
lista_mensaje = lista_mensaje()
app = Flask(__name__)



@app.route('/grabar_mensaje',methods=['POST'])
def grabar_mensaje():
    if 'file' not in request.files:
        #Este código comprueba si se ha enviado un archivo con la solicitud. Si no es así, devuelve un error.
        return jsonify({"state":"Error","message":"No file was sent"})
    file=request.files['file'] #Si se ha enviado un archivo, se almacena en la variable file.
    if file.filename=='':
        print("Error")
        return jsonify({"state":"Error","message":"The file is empty"}) #Si el nombre del archivo está vacío, devuelve un error.
    if file.filename!="mensajes.xml": #Si el nombre del archivo no es mensajes.xml, devuelve un error.
        return jsonify({"state":"Error","message":"The file is not the correct one"})
    #Si el archivo es correcto, se procede a leerlo y lo parsea con la librería ElementTree.
    tree = ET.parse(file)
    root = tree.getroot()
    for mensaje in root.findall("MENSAJE"):
        texto = mensaje.find("TEXTO").text
        fecha = mensaje.find("FECHA").text
        lista_mensaje.add_mensaje(texto,fecha)
    lista_mensaje.recorrer()
    return jsonify({"state":"Perfect","message":"The file was uploaded successfully"})
@app.route('/get_mensaje',methods=['GET'])
def get_mensaje():
    return lista_mensaje.devolver_mensaje()
@app.route('/get_configuracion',methods=['POST'])
def get_config():
    #Este código comprueba si se ha enviado un archivo con la solicitud. Si no es así, devuelve un error.
    if 'file' not in request.files:
        return jsonify({"state":"Error","message":"No file was sent"})
    file=request.files['file']
    if file.filename=='':
        print("Error")
        return jsonify({"state":"Error","message":"The file is empty"})
    if file.filename!="configuracion.xml": #Si el nombre del archivo no es mensajes.xml, devuelve un error.
        return jsonify({"state":"Error","message":"The file is not the correct one"})
    #Si el archivo es correcto, se procede a leerlo y lo parsea con la librería ElementTree.
    tree = ET.parse(file)
    root = tree.getroot()
    print(root.tag)
    for positive in root.findall("sentimientos_positivos"):
        for palabra in positive.findall("palabra"):
            lista_mensaje.add_positivos(palabra.text)
    for negative in root.findall("sentimientos_negativos"):
        for palabra in negative.findall("palabra"):
            lista_mensaje.add_negativos(palabra.text)
    print(lista_mensaje.get_sentimientos())
    return jsonify({"state":"Perfect","message":"The file was uploaded successfully"})
@app.route('/incializar',methods=['POST'])
def inciar():
    #Reinicia el sistema
    lista_mensaje.inicializar()
    lista_mensaje.recorrer()
    print("Sistema reiniciado")
    return jsonify({"state":"Perfect","message":"The list was initialized successfully"})
@app.route('/get_hashtags',methods=['GET'])
def get_hashtags():
    #Devuelve los hashtags
    hashtags=lista_mensaje.devolver_hashtags()
    print(hashtags)
    return jsonify({"state":"Perfect","hashtags":hashtags})
@app.route('/get_menciones',methods=['GET'])
def get_menciones():
    #Devuelve las menciones
    menciones=lista_mensaje.get_menciones()
    print(menciones)
    return jsonify({"state":"Perfect","menciones":menciones})
@app.route('/definir_msj',methods=['GET'])
def definir_msj():
    #Define la naturaleza del mensaje y devuelve si es positivo o negativo
    lista_mensaje.definir_mensaje()
    return lista_mensaje.definir_mensaje()

if __name__ == '__main__':  
    app.run(debug=True,port=5000)

