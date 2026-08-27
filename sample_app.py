import os
from flask import Flask, render_template
import pymysql

app = Flask(__name__)

MYSQL_PASSWORD = "super_secret_123"

@app.route("/")
def home():
    try:
        # Vamos a intentar conectarnos a la base de datos MySQL
        conn = pymysql.connect(
            host="base_datos",
            user="root",
            password=os.environ.get("DB_PASSWORD", ""),
            database="bd_lina",
            connect_timeout=3
        )
        conn.close()
        db_status = "Conexion exitosa a la BD!"
    except Exception as e:
        db_status = f"Error en la conexion: {e}"

    return render_template("index.html", db_status=db_status)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5050, debug=True)  # nosec B104