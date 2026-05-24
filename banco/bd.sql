create database DockerLinux

use DockerLinux

create table Tarefas(
    id int primary key auto_increment,
    titulo varchar(100) not null,
    descricao varchar(255) not null,
    status varchar(50) not null,
    data_criacao datetime default current_timestamp,
    data_atualizado datetime default current_timestamp on update current_timestamp
)

create table Usuarios(
    id int primary key auto_increment,
    nome varchar(100) not null,
    email varchar(100) not null unique,
    senha varchar(255) not null
)

create table Tarefas_Usuarios(
    idTarefa int,
    idUsuario int,
    primary key (idTarefa, idUsuario),
    foreign key (idTarefa) references Tarefas(id) on delete cascade,
    foreign key (idUsuario) references Usuarios(id) on delete cascade
)
