# tests/test_app.py
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from App import app  # Assure-toi que l'import correspond au nom de ton fichier app.py

# Crée une fixture pour initialiser le client de test Flask
@pytest.fixture
def client():
    # Crée une instance de l'application Flask en mode test
    app.config['TESTING'] = True
    client = app.test_client()
    yield client  # Cela nous permet de simuler des requêtes HTTP
    # Aucun nettoyage nécessaire ici, mais si tu en avais besoin, tu pourrais ajouter du code après yield

# Test d'une route GET
def test_get_users(client):
    response = client.get('/users')  # Change l'URL en fonction de ta route
    assert response.status_code == 200  # Vérifie que la réponse est un code 200 (OK)
    assert b"John Doe" in response.data  # Vérifie si "John Doe" est dans la réponse

# Test d'une route POST
def test_post_user(client):
    response = client.post('/users', json={'name': 'Alice', 'age': 28})  # Envoie une requête POST avec un JSON
    assert response.status_code == 201  # Vérifie que la réponse est un code 201 (Créé)
    assert b"Alice" in response.data  # Vérifie si "Alice" est dans la réponse

