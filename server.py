from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)


@app.route('/', methods=['POST'])
def obtener_datos():
    # Obtener los datos de la solicitud POST


    tracking=request.json.get('guia')

    # Extraer la URL de la página web de la solicitud
    url = (f'https://unoexpresspanama.com/track3.php?g={tracking}')

    # Realizar la solicitud GET a la URL
    response = requests.get(url)

    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')

        # Lista de IDs de elementos que deseas encontrar
        ids = ["guia", "fecha", "origen", "destino", "estado", "destinatario", "fechaentrega", "entregadoa"]

        # Crear un diccionario para almacenar los valores
        valores = {}

        # Buscar y extraer los elementos por sus 'ids'
        for elemento_id in ids:
            elemento = soup.find(id=elemento_id)
            valores[elemento_id] = elemento.text if elemento else "No se encontró"

        # Devolver los valores como JSON
        return jsonify(valores)
    else:
        return jsonify({"error": "La solicitud no fue exitosa. Código de respuesta:", }), 400

if __name__ == "__main__":
    app.run(port=port)
