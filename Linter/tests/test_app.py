"""Tests for the student registration application."""

import json

import pytest

from Linter import app as app_module


@pytest.fixture(name="users_file")
def users_file_fixture(tmp_path, monkeypatch):
    """Replace the production users file with an isolated temporary file."""
    temporary_file = tmp_path / "usuarios.json"
    monkeypatch.setattr(app_module, "USERS_FILE", temporary_file)
    return temporary_file


@pytest.fixture(name="client")
def client_fixture():
    """Create a Flask test client."""
    app_module.app.config.update(TESTING=True)
    with app_module.app.test_client() as test_client:
        yield test_client


def test_cargar_usuarios_returns_empty_list_when_file_is_missing(users_file):
    """A missing JSON file should behave like an empty registration list."""
    assert not users_file.exists()
    assert app_module.cargar_usuarios() == []


def test_cargar_usuarios_returns_empty_list_for_invalid_json(users_file):
    """Malformed JSON should not prevent the application from starting."""
    users_file.write_text("not valid json", encoding="utf-8")

    assert app_module.cargar_usuarios() == []


def test_guardar_usuarios_writes_valid_json(users_file):
    """Saved registrations should retain their values and Unicode characters."""
    usuarios = [
        {
            "nombre": "María",
            "apellido": "Gómez",
            "dni": "40123456",
            "legajo": "123456",
            "email": "maria@example.com",
        }
    ]

    app_module.guardar_usuarios(usuarios)

    assert json.loads(users_file.read_text(encoding="utf-8")) == usuarios
    assert "María" in users_file.read_text(encoding="utf-8")


def test_index_displays_registered_user_count(client, users_file):
    """The home page should display the number of saved registrations."""
    users_file.write_text(
        json.dumps([{"nombre": "Ana"}, {"nombre": "Luis"}]),
        encoding="utf-8",
    )

    response = client.get("/")

    assert response.status_code == 200
    assert "2 inscriptos" in response.get_data(as_text=True)


def test_inscripcion_strips_and_saves_form_data(client, users_file):
    """Submitting the form should normalize and persist a new registration."""
    response = client.post(
        "/inscripcion",
        data={
            "nombre": "  Ana ",
            "apellido": " Pérez  ",
            "dni": " 40123456 ",
            "legajo": " 123456 ",
            "email": " ana@example.com ",
        },
    )

    assert response.status_code == 200
    assert "¡Inscripción realizada correctamente!" in response.get_data(as_text=True)
    assert "1 inscripto" in response.get_data(as_text=True)
    assert json.loads(users_file.read_text(encoding="utf-8")) == [
        {
            "nombre": "Ana",
            "apellido": "Pérez",
            "dni": "40123456",
            "legajo": "123456",
            "email": "ana@example.com",
        }
    ]


def test_inscripcion_rejects_an_incomplete_form(client, users_file):
    """An incomplete registration should return a client error and not save data."""
    response = client.post("/inscripcion", data={"nombre": "Ana"})

    assert response.status_code == 400
    assert not users_file.exists()
