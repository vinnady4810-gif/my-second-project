from flask import Flask

# створюємо додаток
app = Flask(__name__)

# головна сторінка
@app.route("/")
def home():
    return "<h1>Привіт, Надія!</h1><p>Це мій перший сайт на Python :)</p>"

# додаткова сторінка
@app.route("/about")
def about():
    return "<h2>Про сайт</h2><p>Цей сайт створений на Flask.</p>"

# запуск сервера
if __name__ == "__main__":
    app.run(debug=True)
