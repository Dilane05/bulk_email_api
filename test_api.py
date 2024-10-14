import requests

url = "http://127.0.0.1:5000/send-newsletter"
data = {
    "contacts": [
        {"name": "John Doe", "email": "angedilane05@gmail.com"},
        {"name": "Jane Smith", "email": "cupidontech3@gmail.com"}
    ],
    "subject": "Newsletter Subject",
    "body": "Hello {name}, welcome to our newsletter!"
}

response = requests.post(url, json=data)

print("Status Code:", response.status_code)
print("Response Body:", response.json())
