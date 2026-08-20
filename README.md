# Actividad práctica — Linter con Python y Ruff

## Gestión de la Calidad de Software

Este proyecto contiene una pequeña aplicación web desarrollada con **Python + Flask** para registrar estudiantes en la materia **Gestión de la Calidad de Software**.

La aplicación funciona, permite completar un formulario desde el navegador y guarda las inscripciones en un archivo JSON local. Sin embargo, el objetivo principal de la actividad no es Flask: el objetivo es utilizar un **linter** para analizar la calidad del código fuente.

---

## 1. Crear un entorno virtual

Antes de instalar las dependencias, crear un entorno virtual dentro del proyecto.

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Cuando el entorno esté activo, instalar las dependencias:

```bash
pip install -r requirements.txt
```

---

## 2. Ejecutar la aplicación

Con el entorno virtual activo, ejecutar:

```bash
python app.py
```

Flask iniciará un servidor local. Abrir el navegador e ingresar a:

```text
http://127.0.0.1:5000
```

---

## 3. Probar el sistema

Antes de trabajar con el linter, utilizar brevemente la aplicación para conocer su comportamiento.

1. Observar la interfaz en el navegador.
2. Completar el formulario con datos de prueba.
3. Realizar al menos **dos inscripciones**.
4. Verificar que aparezca el mensaje de confirmación.
5. Abrir el archivo `usuarios.json`.
6. Comprobar que los usuarios ingresados desde la interfaz hayan quedado almacenados en ese archivo.

> La aplicación guarda los datos únicamente de forma local dentro de este proyecto.

---

# 4. Actividad principal: análisis con Ruff

Un programa puede funcionar correctamente y, al mismo tiempo, contener problemas de calidad en su código.

En esta actividad vamos a utilizar **Ruff**, una herramienta de análisis estático para Python, para detectar algunos de esos problemas.

Detener el servidor Flask si sigue ejecutándose y correr:

```bash
ruff check app.py
```

Ruff mostrará distintos problemas encontrados en el archivo Python.

## Tu tarea

1. Leer cada mensaje informado por Ruff.
2. Identificar la línea donde se encuentra el problema.
3. Observar el código de la regla informada por Ruff.
4. Interpretar qué está indicando esa regla.
5. Corregir manualmente los problemas detectados.
6. Volver a ejecutar:

```bash
ruff check app.py
```

El objetivo es llegar a un resultado sin problemas pendientes.

```text
All checks passed!
```

---

## 5. Verificación final

Una vez corregidos los problemas de linting, volver a ejecutar la aplicación:

```bash
python app.py
```

Abrir nuevamente:

```text
http://127.0.0.1:5000
```

Realizar una nueva inscripción y comprobar que el sistema continúa funcionando correctamente.

La idea es verificar que mejoramos aspectos internos del código sin modificar el comportamiento esperado de la aplicación.

---

## Preguntas de cierre

- ¿La aplicación funcionaba antes de ejecutar Ruff?
- ¿Qué tipo de problemas pudo detectar el linter sin ejecutar la aplicación?
- ¿Corregir los problemas detectados modificó el comportamiento del sistema?
- ¿Qué valor puede aportar una herramienta de linting dentro de un proceso de calidad de software?

---

## Estructura del proyecto

```text
actividad_linter_flask/
├── app.py
├── README.md
├── requirements.txt
├── usuarios.json
├── templates/
│   └── index.html
└── static/
    ├── css/
    │   └── style.css
    └── js/
        └── script.js
```
