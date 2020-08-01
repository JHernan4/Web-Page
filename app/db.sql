CREATE TABLE peliculas(
  id  INTEGER NOT NULL DEFAULT nextval('user_id_seq'),
  title VARCHAR(100) NOT NULL,
  price  DOUBLE NOT NULL,
  sinopsis VARCHAR(100000),
  reparto VARCHAR (100000),
  genero VARCHAR(50) NOT NULL,
  idiomas VARCHAR (1000),
  director VARCHAR (100),
  caratula VARCHAR (200) NOT NULL,
  anio integer,
  CONSTRAINT pelicula_pkey PRIMARY KEY (id)
)

CREATE TABLE usuarios(
  id INTEGER NOT NULL DEFAULT nextval('user_id_seq'),
  username VARCHAR (50) NOT NULL,
  password VARCHAR (50) NOT NULL,
  name VARCHAR (50) NOT NULL,
  surname1 VARCHAR(50) NOT NULL,
  surname2 VARCHAR(50) NOT NULL,
  age INT NOT NULL,
  email VARCHAR (50) NOT NULL,
  phone VARCHAR (25) NOT NULL,
  account VARCHAR (16),
  salary DOUBLE,
  CONSTRAINT user_pkey PRIMARY KEY (id)
)

INSERT INTO peliculas ("title", "price", "sinopsis", "reparto", "genero", "idiomas", "director", "caratula", "anio") values ('Tres Metros sobre el Cielo', 23.99, 'Es la historia de dos jóvenes: uno problemático con tendencias violentas que inicia un romance con una niña rica.', 'Mario Casas, Alvaro Cervantes, Maria Valverde, Marina Salas', 'Comedia Romántica', 'Español', 'Fernando Molina', 'static/imagenes/3MSC.jpg', 2010);
INSERT INTO peliculas ("title", "price", "sinopsis", "reparto", "genero", "idiomas", "director", "caratula", "anio") values ('Torrente, el brazo tonto de la ley"', 12.99, 'Un ex policía le pide ayuda a un amigo al descubrir a una banda de narcotraficantes que opera en un restaurante chino.', 'Santiago Segura, Javier Camara, Neus Asensi, Tony Leblanc, Chus Lampreabe', 'Humor', 'Español', 'Santiago Segura', 'static/imagenes/torrente.jpg', 1998);
INSERT INTO peliculas ("title", "price", "sinopsis", "reparto", "genero", "idiomas", "director", "caratula", "anio") values ('Torrente, misión en Marbella', 16.99, 'Un ex policía decide montar una agencia de investigación al mismo tiempo que intenta recuperar su sitio en la sociedad.', 'Santiago Segura, Gabino Diego, Rossana Walls, Tony Leblanc, INés Sastre', 'Humor', 'Español', 'Santiago Segura', 'static/imagenes/torrente2.jpg', 2001);
INSERT INTO peliculas ("title", "price", "sinopsis", "reparto", "genero", "idiomas", "director", "caratula", "anio") values ('Torrente, El Protector', 16.99, 'Giannina Ricci es una popular eurodiputada que viene de visita a España para cerrar las fábricas de la multinacional Petronosa porque ponen en peligro el medio ambiente. El jefe de la compañía soborna a dos de los encargados de seguridad de la eurodiputada para que puedan ayudarle a planear un ataque contra ella. José Luis Torrente, probablemente uno de los peores policías del mundo, es el encargado de proteger a Ricci.', 'Santiago Segura, Yvonne Scio, JOsé Mota, Tony Leblanc, Javoer Gutierrez', 'Humor', 'Español', 'Santiago Segura', 'static/imagenes/torrente3.jpg', 2005);
INSERT INTO peliculas ("title", "price", "sinopsis", "reparto", "genero", "idiomas", "director", "caratula", "anio") values ('Torrente, Letal Crisis', 16.99, 'Tras varios intentos fallidos de llevar una vida digna, Torrente decide aceptar un peligroso encargo que le hace un viejo conocido. Esto le lleva a afrontar uno de los momentos mas críticos de su carrera cuando le acusan injustamente de un crimen que no ha cometido. Pero esta dispuesto a vengarse de los malhechores que lo engañaron.', 'Santiago Segura, Kiko Rivera, Mara Lapiedra, Tony Leblanc, Javier Gutierrez, Yon Gonzalez', 'Humor', 'Español', 'Santiago Segura', 'static/imagenes/torrente4.jpg', 2011);
INSERT INTO peliculas ("title", "price", "sinopsis", "reparto", "genero", "idiomas", "director", "caratula", "anio") values ('Torrente, Operación Eurovegas', 18.99, 'Torrente sale de la cárcel en el año 2018 para encontrarse una España totalmente diferente de la que él conocía. Ante este shock decide pasar a ser un 'fuera de la ley' y atracar un casino. Gracias a su red de contactos de la cárcel logra localizar a John Marshall, el responsable de la planificación de la seguridad del mayor casino de Eurovegas. Marshall le dice que lo más importante es contar con un equipo de especialistas y Torrente se dispone a encontrarlos entre sus conocidos.', 'Santiago Segura, Neus Asensi, Carlos Areces, Julián Lopez, Alec Baldwin', 'Humor', 'Español', 'Santiago Segura', 'static/imagenes/torrente5.jpg', 2014);
INSERT INTO peliculas ("title", "price", "sinopsis", "genero", "idiomas", "director", "caratula", "anio") values ('Bienvenido, Mister Marshall', 21.99, 'Villar del Río es un pequeño y tranquilo pueblo en el que nunca pasa nada. Sin embargo, el mismo día en que llega la cantante folclórica Carmen Vargas, el alcalde recibe la noticia de la inminente visita de un comité del Plan Marshall. La noticia provoca un gran revuelo entre los vecinos que quieren impresionar y ofrecer a los americanos un recibimiento muy especial.', 'Comedia', 'Español', 'Luis García Berlanga', 'static/imagenes/marshall.jpg', 1953);
INSERT INTO peliculas ("title", "price", "sinopsis", "reparto", "genero", "idiomas", "director", "caratula", "anio") values ('Tengo Ganas de Ti', 23.99, 'Hache pasa unos años en Londres antes de regresar a Barcelona. Él se reúne con Babi y su cariño mutuo sigue presente. Hache decide recuperar su corazón antes de que ella se case con otro hombre.', 'Mario Casas, Mria Valverde, Marina Salas, Lucho Fernandez, Clara Lago, Alvaro Cervantez', 'Comedia Romántica', 'Español', 'Fernando Molina', 'static/imagenes/TGDT.jpg', 2012);
