/*
------
DATABASE PARA EL TIF
------
*/

drop database if exists discord_clone;
CREATE DATABASE IF NOT EXISTS discord_clone;

USE discord_clone;

CREATE TABLE IF NOT EXISTS users(
	user_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR (255) NOT NULL,
    last_name VARCHAR (255) NOT NULL,
    email VARCHAR (255) NOT NULL UNIQUE,
    user_name VARCHAR (255) NOT NULL UNIQUE,
    password VARCHAR (255) NOT NULL,
    date_of_birth DATE NOT NULL,
    profile_picture BLOB
)ENGINE=InnoDB CHARSET = utf8mb4;

CREATE TABLE IF NOT EXISTS servers(
	server_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    server_name VARCHAR (255) NOT NULL UNIQUE,
    description VARCHAR (255) NOT NULL,
    img_server BLOB
)ENGINE=InnoDB CHARSET = utf8mb4;

CREATE TABLE IF NOT EXISTS channels(
	channel_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    channel_name VARCHAR (255) NOT NULL,
    server_id INT NOT NULL,
    FOREIGN KEY (server_id) REFERENCES servers(server_id) ON DELETE CASCADE ON UPDATE CASCADE
)ENGINE=InnoDB CHARSET = utf8mb4;

CREATE TABLE IF NOT EXISTS messages(
	message_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    message TEXT(65535) NOT NULL,
    creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    user_id INT NOT NULL,
    channel_id INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (channel_id) REFERENCES channels(channel_id) ON DELETE CASCADE ON UPDATE CASCADE
)ENGINE=InnoDB CHARSET = utf8mb4;

CREATE TABLE IF NOT EXISTS server_user(
	server_user_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    rol ENUM('Admin', 'Common') NOT NULL,
    server_id INT NOT NULL,
    user_id INT NOT NULL,
    FOREIGN KEY (server_id) REFERENCES servers(server_id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE ON UPDATE CASCADE
)ENGINE=InnoDB CHARSET = utf8mb4;

CREATE TABLE IF NOT EXISTS channel_user(
	channel_user_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    channel_id INT NOT NULL,
    user_id INT NOT NULL,
    FOREIGN KEY (channel_id) REFERENCES channels(channel_id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE ON UPDATE CASCADE
)ENGINE=InnoDB CHARSET = utf8mb4;

/*
------
SELECT
------
*/
SELECT * FROM users;
SELECT * FROM servidores;
SELECT * FROM canales;
SELECT * FROM mensajes;
SELECT * FROM servidor_usuario;

/*
------
ELIMINAR TODO
------
*/
DROP TABLE IF EXISTS usuarios;
DROP TABLE IF EXISTS servidores;
DROP TABLE IF EXISTS canales;
DROP TABLE IF EXISTS mensajes;
DROP TABLE IF EXISTS servidor_usuario;
DROP TABLE IF EXISTS canales_usuarios;
