<div id='id6' />

# USO DE LA API :

# **Índice :**
 ## 1. [Path relacionados a Users](#id1)
 ## 2. [Path relacionados a Servers](#id2)
 ## 3. [Path relacionados a Channels](#id3)
 ## 4. [Path relacionados a Mesages](#id4)
 ## 5. [Path relacionados a Authetication](#id5)

<div id='id1' />

# Path relacionados a Users:

### GET http://127.0.0.1:5000/api/users/id :
Devuelve los datos de un usuario pasando su id en el path y usando el método GET. Ejemplo:

http://127.0.0.1:5000/api/users/1
### GET http://127.0.0.1:5000/api/user_server/id :
Devuelve los servidores creados y a los cuales se encuentra unido un usuario a través de su id. Ejemplo:

http://127.0.0.1:5000/api/user_server/1
### POST http://127.0.0.1:5000/api/users :
Crea un usuario usando el método POST. Los datos deben pasarse por JSON. Los mismos deben ser first_name(string),last_name(string), email(string), user_name(string), password(string) y date_of_birth(string con formato yy/mm/dd). Ejemplo:

content-type: application/json

{
  "first_name":"John",

  "last_name":"Does",

  "email":"johndoe@gmail.com",

  "user_name": "John Doe",

  "password": "asdqwezxcqwe",

  "date_of_birth":"1990-06-15"
}
### PUT http://127.0.0.1:5000/api/users/id :
Actualiza un usuario pasando su id en el path, el contenido a modificar en un JSON y el método PUT. Aquí se puede incluir el campo profile_picture(blob) para que el usuario guarde una imagen de perfil. Ejemplo:

http://127.0.0.1:5000/api/users/1

content-type: application/json

{
"email":"johndoe2@gmail.com"
}
### DELETE http://127.0.0.1:5000/api/users/id :
Elimina un usuario pasando su id en el path y usando el método DELETE. Ejemplo:

DELETE http://127.0.0.1:5000/api/users/1

## [Volver al Inicio](#id6)
---

<div id='id2' />

# Path relacionados a Servers:
### GET http://127.0.0.1:5000/api/servers/id :
Devuelve los datos de un servidor y sus canales en caso de que existan, pasando su id en el path y usando el método GET. Ejemplo:

http://127.0.0.1:5000/api/servers/1
### GET http://127.0.0.1:5000/api/all_servers :
Devuelve todos los servidores existentes en la BD usando el método GET.

### POST http://127.0.0.1:5000/api/servers :
Crea un servidor usando el método POST. Los datos deben pasarse por JSON, los mismos deben ser server_name(string),description(string), user_id(int). Ejemplo:

content-type: application/json

{
  "server_name":"Server de John Doe",
  "description":"Este es un servidor de prueba",
  "user_id":1
}

### POST http://127.0.0.1:5000/api/join_server :
Registra en la entidad user_server cuando un usario se une a un servidor a través del método POST. Los datos deben pasarse por un JSON, los mismos deben ser user_id(int) y server_id(int). Ejemplo:

content-type: application/json

{
  "user_id":1,
  "server_id":1
}

### PUT http://127.0.0.1:5000/api/servers/id :
Actualiza un servidor pasando su id en el path, el contenido a modificar en un JSON y el método PUT. Aquí se puede incluir el campo img_server(blob) para que el usuario guarde una imagen del servidor. Ejemplo:

http://127.0.0.1:5000/api/servers/1

content-type: application/json

{
  "description":"Server donde hablamos de JJK y Anime en general"
}

### DELETE http://127.0.0.1:5000/api/servers/id :
Elimina un servidor pasando su id en el path y usando el método DELETE. Ejemplo:

http://127.0.0.1:5000/api/servers/14

## [Volver al Inicio](#id6)
---

<div id='id3' />

# Path relacionados a Channels:
### GET http://127.0.0.1:5000/api/channels/id :
Devuelve un canal y los mensajes dentros del mismo, pasando su id en el path y usando el método GET. Ejemplo. 

http://127.0.0.1:5000/api/channels/1

### GET http://127.0.0.1:5000/api/show_channels :
Devuelve los canales de un servidor y el rol del usuario en ese servidor usando el método GET. EL contenido de la consulta debe pasarse por un JSON que debe incluir user_id(int) y server_id(int). Ejemplo: 

content-type: application/json

{
  "user_id": 6,
  "server_id":14
}

### GET http://127.0.0.1:5000/api/total_msgs/id :
Devuelve el total de mensajes de un canal. Recibe como parametro en la URL el id del canal a consultar. Ejemplo:

http://127.0.0.1:5000/api/total_msgs/1

### POST http://127.0.0.1:5000/api/channels :
Crea un canal usando el método POST. Los datos deben pasarse a través de un JSON, que debe incluir channel_name(str) y server_id(int), este último es el id del servidor en donde se crea el canal. Ejemplo:

content-type: application/json

{
  "channel_name": "Canal 1 de prueba",
  "server_id":1
}

### PUT http://127.0.0.1:5000/api/channels/id :
Permite actualizar un canal pasando el id del mismo en el path a través del método PUT. Además debe pasarse el contenido a modificar en un JSON. Ejemplo:

http://127.0.0.1:5000/api/channels/1

content-type: application/json

{
  "channel_name": "Canal 1 de prueba Modificado"
}

### DELETE http://127.0.0.1:5000/api/channels/id :
Elimina un canal pasando el id del mismo en el path a través del método DELETE. Ejemplo:

http://127.0.0.1:5000/api/channels/1

## [Volver al Inicio](#id6)
---

<div id='id4' />

# Path relacionados a Mesages
### GET http://127.0.0.1:5000/api/messages/id : 
Devuelve un mensaje por su id usando el método GET. El id debe ser especificado en el path. Ejemplo:

http://127.0.0.1:5000/api/messages/1

### POST http://127.0.0.1:5000/api/messages :
Permite crear un mensaje usando el método post. Los datos deben pasarse a través de un JSON y deben incluir: message(str), channel_id(int), user_id(int). Ejemplo:

content-type: application/json

{
  "message":"Prueba de insertar mensaje en el canal 1",
  "channel_id":1,
  "user_id":1
}

### PUT http://127.0.0.1:5000/api/messages/id :
Permite modificar un mensaje a usando el método PUT. Debe pasarse por la ruta el id del mensaje que se quiere modificar y en un JSON los datos a cambiar. Ejemplo:

http://127.0.0.1:5000/api/messages/1

content-type: application/json

{
  "message":"Se modificó el mensaje anterior"
}

### DELETE http://127.0.0.1:5000/api/messages/id :
Permite elimianr un mensaje a través del método DELETE. Se debe pasar el id del mensaje a eliminar a través del path. Ejemplo:

http://127.0.0.1:5000/api/messages/1

## [Volver al Inicio](#id6)
---

<div id='id5' />

# Path relacionados a Authentication

### POST http://127.0.0.1:5000/auth/login :
Permite iniciar sesión a través del método POST. Se debe pasar un JSON con los datos user_name(str) y password(str). Ejemplo:

http://127.0.0.1:5000/auth/login

content-type: application/json

{
"user_name":"John Doe",
"password":"asdqwezxcqwe"
}

### GET http://127.0.0.1:5000/auth/profile :
Devuelve los datos del usuario que inicia sesión

### GET http://127.0.0.1:5000/auth/logout :
Cierra la sesión del usuario.

## [Volver al Inicio](#id6)
---