# AGENDA MONGO
## Que es?
- Agenda Mongo es una web-app que se utiliza como una aplicación para guardar notas.
  
- Con este proyecto he practicado las siguientes tecnologías:
    - Conexión a una base de datos **NO** relacional como es Mongo DB.
    - **Python**, utilizando la librería **Flask** y sus plantillas.
    - **Bulma** como librería CSS. 
    - Además esta aplicación cuenta con un fichero **Procfile** para poder ejecutar la aplicación en **Heroku**.

## Como arrancar la web en mi local?
- Para arrancar esta web en tu local lo mas recomendable es generar un entorno virtual con Python, para no fastidiar nuestra librería general de dependencias.
- Para ello, en una terminal (cmd) y en la ruta del proyecto seguiremos los siguientes pasos:
    - ``python -m venv env`` : Este comando nos creará un entorno virtual dentro del proyecto.
    - ``env\Scripts\activate``: Activamos el entorno virtual, nos aparecerá **(env)** detrás de la ruta en la consola.
    - ``pip install -r requirements.txt``: Instalamos las dependencias correspondientes que vienen fijadas en el archivo **requirements.txt**.
    - ``python main.py``: Arrancamos el proyecto.
    - Estará corriendo en el puerto: **localhost:5000**.
Sencillo no?