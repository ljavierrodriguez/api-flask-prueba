# Comandos para flask migrate

- Habilitar comando flask
```shell
export FLASK_APP=app.py
```

- Generar la carpeta migrations
```shell
flask db init
```
- Crear migrations
```shell
flask db migrate
```
- Enviar Migraciones a la Base de Datos
```shell
flask db upgrade
```

# Generar o Actualizar el archivo requirements.txt

```shell
pip freeze > requirements.txt
```