from flask import Flask, request, jsonify, render_template
import google.generativeai as genai
import os
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv('config.env')
API_KEY = os.getenv('API_KEY')

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel('gemini-pro')


with open('./static/docs/arquivo.txt', 'r', encoding='utf-8') as arquivo:
    
    CONTEXT = arquivo.read()



@app.route('/', methods=['GET', 'POST'])
def index():
    
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process_input():
    # Recebe o input do JavaScript
    data = request.json
    userQuestion = data.get('question')
    
    fullQuestion = f"Com base no texto a seguir, responda a pergunta:\n{CONTEXT}\nPergunta: {userQuestion}"
    
    response = model.generate_content(fullQuestion)
    
    response_text = response.candidates[0].content.parts[0].text

    return jsonify({'result': response_text})   


@app.route('/newDocumentForm', methods=['GET', 'POST'])
def new_document():
    # Recebe o input do JavaScript
    if request.method == 'POST':
        
        data = request.get_json()
        
        titulo = data.get('title')
        autor = data.get('author')
        conteudo = data.get('content')
        
        print(f"Título: {titulo}\nAutor: {autor}\nConteúdo: {conteudo}")
    
    return render_template('newDocumentForm.html')


if __name__ == '__main__':
    app.run(debug=True)