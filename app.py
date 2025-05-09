from flask import Flask, render_template, request
from scraper import get_headlines

app = Flask(__name__)

@app.route('/')
def home():
    try:
        noticias = get_headlines()
    except Exception as e:
        return f"Erro ao acessar as manchetes: {e}", 500

    return render_template('noticias.html', noticias=noticias)

@app.route('/buscar')
def buscar():
    query = request.args.get('q', '').lower()
    try:
        todas = get_headlines()
    except Exception as e:
        return f"Erro: {e}", 500

    filtradas = [n for n in todas if query in n['title'].lower()]
    return render_template('noticias.html', noticias=filtradas)

if __name__ == '__main__':
    app.run(debug=True)
