# Importante:
## 1. Para usar la API se deben installar los paquetes necesarios, para ello ejecutar el siguiente comando:
pip install -r "requirements.txt"
## 2. Se debe crear un un archivo .env que contendrá las variables de entorno. Estas variables serán:
* SECRET_KEY = tu clave secreta para el manejo de sesiones
* DATABASE_USERNAME = tu nombre de usuario en mysql
* DATABASE_PASSWORD = tu contraseña en mysql
* DATABASE_HOST = tu host de mysql
* DATABASE_PORT = tu puerto de mysql
* DATABASE_NAME = "discord_clone"

Nota: el nombre de la BD va incluida pero se puede cambiar a través del script de ejecución mencionado en el inciso siguiente.

## 3. En la carpeta sql/ se encontrará el archivo DB_TIF.sql, este debe ejecutarse para crear la Base de Datos.

## 4. Para iniciar la API se debe ejecutar el archivo run.py.

## 5. En el archivo api.md se encuentra la documentación para utilizar la API.