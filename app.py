from flask import Flask, request, jsonify
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

app = Flask(__name__)

# Configuration pour l'envoi d'emails
SMTP_SERVER = 'smtp.hostinger.com'  # Remplace avec ton serveur SMTP
SMTP_PORT = 465
SMTP_USERNAME = 'newsletter@cil-labs.com'
SMTP_PASSWORD = '>Zd6FLSL[r>'

# Fonction pour envoyer des emails en masse
def send_bulk_emails(contacts, subject, body):
    try:
        # Connexion au serveur SMTP en utilisant SSL
        server = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
        server.login(SMTP_USERNAME, SMTP_PASSWORD)

        for contact in contacts:
            # Configuration du message
            msg = MIMEMultipart()
            msg['From'] = SMTP_USERNAME
            msg['To'] = contact['email']
            msg['Subject'] = subject

            # Le contenu du mail
            message = body.format(name=contact['name'])
            msg.attach(MIMEText(message, 'plain'))

            # Envoi de l'email
            server.send_message(msg)
            print(f"Email sent to {contact['name']} at {contact['email']}")
        
        # Fermeture de la connexion
        server.quit()

        return True, "Emails sent successfully !"
    except Exception as e:
        return False, str(e)

# Route API pour envoyer les emails
@app.route('/send-newsletter', methods=['POST'])
def send_newsletter():
    data = request.get_json()

    # Extraction des paramètres
    contacts = data.get('recipients')  # Change 'contacts' à 'recipients'
    subject = data.get('subject')
    body = data.get('message')  # Change 'body' à 'message'

    # Validation des données
    if not contacts or not subject or not body:
        return jsonify({"error": "Missing contacts, subject or body"}), 400

    success, message = send_bulk_emails(contacts, subject, body)
    
    if success:
        return jsonify({"message": message}), 200
    else:
        return jsonify({"error": message}), 500

if __name__ == '__main__':
    app.run(debug=True)
