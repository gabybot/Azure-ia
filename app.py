from flask import Flask, render_template, request
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
from dotenv import load_dotenv
import os

# Cargar variables de entorno
load_dotenv()

app = Flask(__name__)

endpoint = os.getenv('AZURE_TEXT_ANALYTICS_ENDPOINT')
key = os.getenv('AZURE_TEXT_ANALYTICS_KEY')

def authenticate_client():
    ta_credential = AzureKeyCredential(key)
    client = TextAnalyticsClient(endpoint=endpoint, credential=ta_credential)
    return client

def detect_language(client, text):
    response = client.detect_language(documents=[{"id": "1", "text": text}])
    return response[0].primary_language.name

@app.route('/')
def home():
    return render_template('index.html')  

@app.route('/detect', methods=['POST'])
def detect():
    client = authenticate_client()
    text = request.form['text'] 
    language = detect_language(client, text)
    return render_template('result.html', text=text, language=language)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
