# 🖥️ Flask Language Detection App - Azure AI Text Analytics 🌐

## 🇬🇧 English

### 📖 Description

This project is a web application built with **Flask** that uses **Azure AI Text Analytics** to detect the language of a text entered by the user. The app sends the input text to Azure AI services and displays the detected language on the result page. The front-end is designed using HTML and CSS, with a clean and modern style.

### 🚀 Features

- 📝 **Text Input**: Users can input any text to detect its language.
- 🌍 **Language Detection**: Uses Azure AI's Text Analytics API to accurately detect the language of the text.
- 💻 **Frontend and Backend**: Built using Flask for the backend and a simple HTML/CSS interface for the frontend.
- 📊 **Responsive Design**: Optimized for both desktop and mobile use.
  
### ⚙️ Setup Instructions

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo

- Create and activate a virtual environment:
For windows:

   python -m venv venv
venv\Scripts\activate

for macOS/linux

python3 -m venv venv
source venv/bin/activate

- Install the dependencies:
pip install -r requirements.txt

- Create a .env file in the root directory with the following content:
AZURE_TEXT_ANALYTICS_ENDPOINT=https://<your-endpoint>.cognitiveservices.azure.com/
AZURE_TEXT_ANALYTICS_KEY=<your-api-key>
- Run the Flask app:
python app.py

Access the app:

Open a browser and navigate to http://127.0.0.1:5000.

🛠️ Technologies Used
Flask: Python web framework.
Azure AI Text Analytics: API for language detection.
HTML/CSS: Front-end design.

🇪🇸 Español
📖 Descripción
Este proyecto es una aplicación web construida con Flask que utiliza Azure AI Text Analytics para detectar el idioma de un texto ingresado por el usuario. La aplicación envía el texto ingresado a los servicios de Azure AI y muestra el idioma detectado en la página de resultados. El front-end está diseñado usando HTML y CSS, con un estilo moderno y limpio.

🚀 Características
📝 Entrada de Texto: Los usuarios pueden ingresar cualquier texto para detectar su idioma.
🌍 Detección de Idioma: Utiliza la API de Text Analytics de Azure AI para detectar con precisión el idioma del texto.
💻 Frontend y Backend: Construido usando Flask para el backend y una interfaz simple de HTML/CSS para el frontend.
📊 Diseño Responsivo: Optimizado para uso tanto en escritorio como en móvil.