# Bulk Email API

## Description
Cette API permet d'envoyer des emails en masse à une liste de contacts avec leur nom personnalisé, en utilisant Flask et un serveur SMTP.

## Endpoints

### 1. Envoyer des emails
- **URL** : `/send-newsletter`
- **Méthode** : `POST`
- **Contenu attendu (JSON)** :
  ```json
  {
      "contacts": [
          {"name": "John Doe", "email": "john@example.com"},
          {"name": "Jane Smith", "email": "jane@example.com"}
      ],
      "subject": "Newsletter Subject",
      "body": "Hello {name}, welcome to our newsletter!"
  }


### 2.Réponse (Succès) :

json
Copy code
{
    "message": "Emails sent successfully!"
}

### 3.Réponse (Erreur) :

json
Copy code
{
    "error": "Description of the error"
}

### 4.Installation
Clonez le projet :

bash
Copy code
git clone https://github.com/ton-username/bulk_email_api.git
cd bulk_email_api
Créez et activez un environnement virtuel :

bash
Copy code
python -m venv venv
venv\Scripts\activate
Installez les dépendances :

bash
Copy code
pip install -r requirements.txt
Exécutez le projet :

bash
Copy code
python app.py
