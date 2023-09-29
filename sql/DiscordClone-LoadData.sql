USE discord_clone;

INSERT INTO users(first_name,last_name,email,user_name,password,date_of_birth) 
	VALUES ("John","Doe","johndoe@gmail.com","John Doe","andapayabobo","1990-06-03");
    
INSERT INTO servers(server_name,description) 
	VALUES ("Server de John", "Servidor dedicado a hablar de programacion");

INSERT INTO channels (channel_name,server_id) 
	VALUES ("Python",1);

INSERT INTO server_user(rol, server_id, user_id) 
	VALUES ("Admin",1,1);

INSERT INTO messages(message,user_id,channel_id) 
	VALUES ("Hello World",1,1);