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

if __name__ == '__main__':  
    app.run(debug=True,port=5000)

