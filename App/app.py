from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Liste des utilisateurs pour la démonstration
users = []

@app.route('/')
def home():
    return render_template('index.html', users=users)

@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        # Ajouter un nouvel utilisateur à la liste
        users.append({'name': name, 'email': email})
        return redirect(url_for('home'))  # Rediriger vers la page d'accueil après l'ajout
    return render_template('add_user.html')

if __name__ == '__main__':
    app.run(debug=True)

