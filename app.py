from flask import Flask, jsonify, request
from flask_cors import CORS
import xml.etree.ElementTree as ET
from mensajes.lista_mensaje import lista_mensaje
lista_mensaje = lista_mensaje()
positivos=[]
negativos=[]
app = Flask(__name__)



@app.route('/grabar_mensaje',methods=['POST'])
def grabar_mensaje():
    if 'file' not in request.files:
        return jsonify({"state":"Error","message":"No file was sent"})
    file=request.files['file']
    if file.filename=='':
        print("Error")
        return jsonify({"state":"Error","message":"The file is empty"})
    if file.filename!="mensajes.xml":
        return jsonify({"state":"Error","message":"The file is not the correct one"})
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
    mensajes=lista_mensaje.devolver_mensaje()
    print(mensajes)
    return jsonify({"state":"Perfect","messages":mensajes})
@app.route('/get_configuracion',methods=['POST'])
def get_config():
    if 'file' not in request.files:
        return jsonify({"state":"Error","message":"No file was sent"})
    file=request.files['file']
    if file.filename=='':
        print("Error")
        return jsonify({"state":"Error","message":"The file is empty"})
    if file.filename!="configuracion.xml":
        return jsonify({"state":"Error","message":"The file is not the correct one"})
    tree = ET.parse(file)
    root = tree.getroot()
    print(root.tag)
    for positive in root.findall("sentimientos_positivos"):
        for palabra in positive.findall("palabra"):
            positivos.append(palabra.text)
    for negative in root.findall("sentimientos_negativos"):
        for palabra in negative.findall("palabra"):
            negativos.append(palabra.text)
    print("positivos: ",positivos)
    print("negativos: ",negativos)
    return jsonify({"state":"Perfect","message":"The file was uploaded successfully"})
@app.route('/incializar',methods=['POST'])
def inciar():
    lista_mensaje.inicializar()
    positivos.clear()
    negativos.clear()
    lista_mensaje.recorrer()
    print("Sistema reiniciado")
    return jsonify({"state":"Perfect","message":"The list was initialized successfully"})
@app.route('/get_hashtags',methods=['GET'])
def get_hashtags():
    hashtags=lista_mensaje.devolver_hashtags()
    print(hashtags)
    return jsonify({"state":"Perfect","hashtags":hashtags})
@app.route('/get_menciones',methods=['GET'])
def get_menciones():
    menciones=lista_mensaje.get_menciones()
    print(menciones)
    return jsonify({"state":"Perfect","menciones":menciones})
if __name__ == '__main__':  
    app.run(debug=True,port=5000)

