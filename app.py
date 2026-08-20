from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return "<h1>¡Hola, Docker y Nginx!</h1><p>Despliegue automático actualizado el 20 de agosto de 2026 🚀</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)