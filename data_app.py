from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Bonjour, bienvenue sur mon application web !"

if __name__ == '__main__':
    app.run(debug=True)