from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return "Error", 500
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=False)  # nosec B104