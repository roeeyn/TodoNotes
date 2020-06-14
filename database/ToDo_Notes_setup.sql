create database if not exists TODO_NOTES collate latin1_swedish_ci;

USE TODO_NOTES;

create table if not exists categories
(
	id int auto_increment
		primary key,
	name varchar(255) null,
	created_at datetime null,
	updated_at datetime null
);

create table if not exists users
(
	id int auto_increment
		primary key,
	username varchar(255) null,
	password varchar(255) null,
	email varchar(255) null,
	created_at datetime null,
	updated_at datetime null
);

create table if not exists notes
(
	id int auto_increment
		primary key,
	title varchar(255) null,
	description varchar(255) null,
	status int null,
	deadline datetime null,
	category_id int default 1 null,
	user_id int null,
	created_at datetime null,
	updated_at datetime null,
	constraint notes_ibfk_1
		foreign key (category_id) references categories (id),
	constraint notes_ibfk_2
		foreign key (user_id) references users (id)
);

create index category_id
	on notes (category_id);

create index user_id
	on notes (user_id);


INSERT INTO TODO_NOTES.categories (id, name, created_at, updated_at) VALUES (1, 'Trabajo', '2020-06-14 18:08:38', '2020-06-14 18:08:38');
INSERT INTO TODO_NOTES.categories (id, name, created_at, updated_at) VALUES (2, 'Hogar', '2020-06-14 18:41:04', '2020-06-14 18:41:04');

INSERT INTO TODO_NOTES.users (id, username, password, email, created_at, updated_at) VALUES (1, 'pedrito', '$2b$12$SIseebNL.7a3BIV6K7xYSOk5GD8FT5xrHatX2.Hu2GP3QHqUzyy9a', 'hola@pedrito.com', '2020-06-14 17:10:49', '2020-06-14 17:10:49');

INSERT INTO TODO_NOTES.notes (id, title, description, status, deadline, category_id, user_id, created_at, updated_at) VALUES (1, 'Barrer', 'barrer toda la sala', 0, '2020-09-21 23:59:59', 1, 1, '2020-06-14 18:12:32', '2020-06-14 18:12:32');
INSERT INTO TODO_NOTES.notes (id, title, description, status, deadline, category_id, user_id, created_at, updated_at) VALUES (2, 'Trapear', 'Trapear toda la sala', 0, '2020-09-21 23:59:59', 2, 1, '2020-06-14 18:41:30', '2020-06-14 18:41:30');