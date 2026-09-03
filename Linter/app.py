"""Flask application providing the application's HTTP endpoints."""

import json
from pathlib import Path

from flask import Flask, render_template, request

app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent
USERS_FILE = BASE_DIR / "usuarios.json"


def cargar_usuarios():
    """Load users from the JSON file."""
    try:
        with USERS_FILE.open("r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def guardar_usuarios(usuarios):
    """Save users to the JSON file."""
    with USERS_FILE.open("w", encoding="utf-8") as archivo:
        json.dump(usuarios, archivo, indent=2, ensure_ascii=False)


@app.route("/")
def index():
    """Render the index page with the total number of registered users."""
    usuarios = cargar_usuarios()
    return render_template("index.html", total_inscriptos=len(usuarios))


@app.route("/inscripcion", methods=["POST"])
def inscripcion():
    """Handle user registration and save the data to the JSON file."""
    usuarios = cargar_usuarios()

    nuevo_usuario = {
        "nombre": request.form["nombre"].strip(),
        "apellido": request.form["apellido"].strip(),
        "dni": request.form["dni"].strip(),
        "legajo": request.form["legajo"].strip(),
        "email": request.form["email"].strip(),
    }

    usuarios.append(nuevo_usuario)
    guardar_usuarios(usuarios)


    return render_template(
        "index.html",
        mensaje="¡Inscripción realizada correctamente!",
        total_inscriptos=len(usuarios),
    )


if __name__ == "__main__":
    app.run(debug=True)
