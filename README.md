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
