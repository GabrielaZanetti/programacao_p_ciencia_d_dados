drop database if exists populacao;

/* cria o banco de dados */
create database populacao;

use populacao;

create table estado (
    uf char(2) not null,
    cod_uf int not null,
    primary key (cod_uf)
);

create table municipios (
    num_muni int not null auto_increment,
    cod_municipio int not null,
    nome_municipio varchar(30) not null,
    populacao int not null,
    cod_uf int not null,
    primary key (num_muni),
    foreign key (cod_uf)
        references estado (cod_uf)
);