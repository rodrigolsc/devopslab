from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Rodrigo Laugeni Scolfaro Caporici"

if __name__ == '__main__':
    app.run()