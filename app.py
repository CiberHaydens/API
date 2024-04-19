from flask import Flask, jsonify

app = Flask(__name__)

# Datos de ejemplo de usuarios
usuarios = [
    {"id": 1, "nombre": "Juan", "edad": 30},
    {"id": 2, "nombre": "María", "edad": 25},
    {"id": 3, "nombre": "Pedro", "edad": 35}
]

# Ruta para obtener una lista de usuarios
@app.route('/usuarios', methods=['GET'])
def obtener_usuarios():
    return jsonify(usuarios)

# Ruta para obtener información detallada sobre un usuario específico
@app.route('/usuarios/<int:id>', methods=['GET'])
def obtener_usuario(id):
    usuario = next((usuario for usuario in usuarios if usuario['id'] == id), None)
    if usuario:
        return jsonify(usuario)
    else:
        return jsonify({"mensaje": "Usuario no encontrado"}), 404

if __name__ == '__main__':
    app.run(debug=True)
