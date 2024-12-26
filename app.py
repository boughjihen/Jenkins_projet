from flask import Flask, jsonify, request

app = Flask(__name__)

# Simuler une base de données
users = [
    {"id": 1, "name": "John Doe", "age": 30},
    {"id": 2, "name": "Jane Smith", "age": 25},
]

# Récupérer tous les utilisateurs
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

# Récupérer un utilisateur par ID
@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    user = next((u for u in users if u['id'] == id), None)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

# Créer un nouvel utilisateur
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if 'name' in data and 'age' in data:
        new_user = {"id": len(users) + 1, "name": data['name'], "age": data['age']}
        users.append(new_user)
        return jsonify(new_user), 201
    return jsonify({"error": "Invalid data"}), 400

# Mettre à jour un utilisateur
@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    data = request.get_json()
    user = next((u for u in users if u['id'] == id), None)
    if user:
        user.update(data)
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

# Supprimer un utilisateur
@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    global users
    users = [u for u in users if u['id'] != id]
    return jsonify({"message": "User deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)
