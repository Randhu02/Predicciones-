# backend.py
from flask import Flask, jsonify, request
import pandas as pd
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Permite todas las solicitudes cross-origin, útil para desarrollo

# Carga datos global (puedes optimizar con cache)
def cargar_datos(version):
    if version == "Prediccion para Tubos - Paquetes":
        df_cemento = pd.read_excel('C:/Users/Usuario/Desktop/PROYECTO TISUR/07_Prediccion_Cemento_Asfaltico.xlsx')
        df_bobinas = pd.read_excel('C:/Users/Usuario/Desktop/PROYECTO TISUR/07_Prediccion_Bobinas.xlsx')
        df_rollos = pd.read_excel('C:/Users/Usuario/Desktop/PROYECTO TISUR/07_Prediccion_Rollos.xlsx')
        df_tubos = pd.read_excel('C:/Users/Usuario/Desktop/PROYECTO TISUR/07_Prediccion_Tubos_Paquetes.xlsx')
    elif version == "Prediccion para Cemento Asfaltico":
        df_cemento = pd.read_excel('C:/Users/Usuario/Desktop/PROYECTO TISUR/06_Prediccion_Cemento_Asfaltico.xlsx')
        df_bobinas = pd.read_excel('C:/Users/Usuario/Desktop/PROYECTO TISUR/06_Prediccion_Bobinas.xlsx')
        df_rollos = pd.read_excel('C:/Users/Usuario/Desktop/PROYECTO TISUR/06_Prediccion_Rollos.xlsx')
        df_tubos = pd.read_excel('C:/Users/Usuario/Desktop/PROYECTO TISUR/06_Prediccion_Tubos_Paquetes.xlsx')       
    elif version == "Prediccion para Bobinas":
        df_cemento = pd.read_excel('C:/Users/Usuario/Desktop/PROYECTO TISUR/03_Prediccion_Cemento_Asfaltico.xlsx')
        df_bobinas = pd.read_excel('C:/Users/Usuario/Desktop/PROYECTO TISUR/03_Prediccion_Bobinas.xlsx')
        df_rollos = pd.read_excel('C:/Users/Usuario/Desktop/PROYECTO TISUR/03_Prediccion_Rollos.xlsx')
        df_tubos = pd.read_excel('C:/Users/Usuario/Desktop/PROYECTO TISUR/03_Prediccion_Tubos_Paquetes.xlsx')          
    elif version == "Prediccion para Rollos":
        df_cemento = pd.read_excel('C:/Users/Usuario/Desktop/PROYECTO TISUR/04_Prediccion_Cemento_Asfaltico.xlsx')
        df_bobinas = pd.read_excel('C:/Users/Usuario/Desktop/PROYECTO TISUR/04_Prediccion_Bobinas.xlsx')
        df_rollos = pd.read_excel('C:/Users/Usuario/Desktop/PROYECTO TISUR/04_Prediccion_Rollos.xlsx')
        df_tubos = pd.read_excel('C:/Users/Usuario/Desktop/PROYECTO TISUR/04_Prediccion_Tubos_Paquetes.xlsx')             
    # Agrega aquí los otros casos...
    else:
        return None, None, None, None
    return df_cemento, df_bobinas, df_rollos, df_tubos

@app.route('/api/datos', methods=['GET'])
def obtener_datos():
    version = request.args.get('version')
    producto = request.args.get('producto')
    area = request.args.get('area')

    dfs = cargar_datos(version)
    if any(df is None for df in dfs):
        return jsonify({"error": "Versión no soportada"}), 400

    df_cemento, df_bobinas, df_rollos, df_tubos = dfs
    mapping = {
        "Cemento": df_cemento,
        "Bobinas": df_bobinas,
        "Rollos": df_rollos,
        "Tubos": df_tubos
    }

    df = mapping.get(producto)
    if df is None:
        return jsonify({"error": "Producto no válido"}), 400

    # Filtra por área si está definido
    if area:
        df = df[df['Área'] == area]

    # Convierte a dict para enviar JSON (puedes limitar filas si es necesario)
    data = df.to_dict(orient='records')
    return jsonify(data)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render asigna el puerto en esta variable
    app.run(host="0.0.0.0", port=port, debug=True)
