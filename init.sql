DROP DATABASE IF EXISTS DockerLinux;
CREATE DATABASE DockerLinux;

USE DockerLinux;

create table Usuarios(
    id int primary key auto_increment,
    nome varchar(100) not null,
    email varchar(100) not null unique,
    senha varchar(255) not null
)

create table Tarefas(
    id int primary key auto_increment,
    titulo varchar(100) not null,
    descricao varchar(255) not null,
    status boolean not null,
    idUsuario int not null,
    data_criacao datetime default current_timestamp,
    data_atualizado datetime default current_timestamp on update current_timestamp,
    foreign key (idUsuario) references Usuarios(id)
)

