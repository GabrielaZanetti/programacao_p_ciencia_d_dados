/* exclui o banco de dados */
drop database if exists estoque;

/* cria o banco de dados */
create database estoque;

use estoque;

/* exclui as tabelas */
create table tipo_cliente (
    id_tipo_cliente int not null auto_increment,
    descr_tipo_cliente varchar(30),
    primary key (id_tipo_cliente)
);

/* cria tabela de cliente      */
create table cliente (
    id_cliente int not null auto_increment,
    nome_cliente char(30),
    id_tipo_cliente int not null,
    primary key (id_cliente),
    foreign key (id_tipo_cliente)
        references tipo_cliente (id_tipo_cliente)
        on update no action on delete restrict
);

/* cria tabela de vendedor     */
create table vendedor (
    id_vendedor int not null auto_increment,
    nome_vendedor char(30),
    pc_comissao decimal(5 , 2 ),
    primary key (id_vendedor)
);

/* cria tabela grupos de itens */
create table grupo (
    id_grupo int not null auto_increment,
    nome_grupo varchar(30),
    primary key (id_grupo)
);

/* cria tabela item de estoque */
create table item (
    id_grupo int not null,
    id_item int not null,
    nome_item char(40) not null,
    unidade char(5),
    preco decimal(9 , 2 ),
    qtde_estoque int,
    primary key (id_grupo , id_item),
    foreign key (id_grupo)
        references grupo (id_grupo)
        on update restrict on delete restrict
);

/* cria tabela de notas fiscais de venda */
create table venda (
    id_venda int not null auto_increment,
    id_vendedor int not null,
    id_cliente int not null,
    dt_venda date not null,
    vl_total_venda decimal(9 , 2 ),
    primary key (id_venda),
    foreign key (id_cliente)
        references cliente (id_cliente)
        on update restrict on delete restrict,
    foreign key (id_vendedor)
        references vendedor (id_vendedor)
        on update restrict on delete restrict
);

/* cria tabela de itens das notas fiscais */
create table item_venda (
    id_venda int not null,
    id_grupo int not null,
    id_item int not null,
    qtde int not null,
    valor decimal(9 , 2 ),
    primary key (id_venda , id_grupo , id_item),
    foreign key (id_grupo , id_item)
        references item (id_grupo , id_item)
        on update restrict on delete restrict
);

/* carga de dados para as tabelas        */
insert into grupo values (7,'eletronicos');
insert into grupo values (4,'livraria');
insert into grupo values (5,'informatica');
insert into grupo values (1,'artigos esportivos');

/* grupo 5 informatica */
insert into item values(5,1,'cartucho canon bc-02','und',72.50,20);
insert into item values(5,2,'cartucho epson 20093','und',65.10,10);
insert into item values(5,3,'cartucho hp 51629a','und',45.28,17);
insert into item values(5,36,'papel form. 80 1v br.c/3000 sp','cxa',55.79,6);
insert into item values(5,31,'refil impr.extr.8508 51649a c1','cjt',19.39,7);
insert into item values(5,47,'toner hp c 7115a p/laser 1200','und',245.61,3);
insert into item values(5,50,'mouse clone c/saida serial','und',5.33,3);
/* grupo 4 livraria */
insert into item values(4,1,'cola tenaz  500grs','tbo',2.50,20);
insert into item values(4,31,'caneta esfer.parker','pc',5.80,3);
insert into item values(4,33,'agenda','pc',6.54,8);
insert into item values(4,4,'album','pc',12.78,12);
insert into item values(4,41,'regua metal','und',1.78,81);
/* grupo 7 eletronicos */
insert into item values(7,2,'dvd','und',1222.50,2);
insert into item values(7,4,'televisao 14 pol.','pc',445.80,3);
insert into item values(7,8,'playstation','pc',512.78,8);

insert into tipo_cliente values (5,'comercio');
insert into tipo_cliente values (6,'arquitetura');
insert into tipo_cliente values (7,'informatica');
insert into tipo_cliente values (8,'industria');
insert into tipo_cliente values (10,'banco');

insert into cliente values (1,'ada lovelace',7);
insert into cliente values (2,'frederick taylor',8);
insert into cliente values (3,'george boole',5);
insert into cliente values (4,'blaise pascal',6);
insert into cliente values (5,'alan turing',10);
insert into cliente values (7,'john von neumann',7);
insert into cliente values (9,'charles babbage',6);

insert into vendedor values (1,'maria elisa ange',9.00);
insert into vendedor values (4,'lucas zardo dos reis',10.00);
insert into vendedor values (5,'claudiomiro a nunes',8.00);
insert into vendedor values (15,'silvia maria',6.00);
insert into vendedor values (10,'mirna s riat',6.00);
insert into vendedor values (11,'mara l batista',4.00);

insert into venda values (441,1,5,'2014-10-01',123.44);
insert into venda values (442,4,2,'2014-06-20',58.14);
insert into venda values (12941,5,3,'2014-01-13',28.49);
insert into venda values (12942,5,3,'2014-03-14',1921.72);
insert into venda values (541,1,4,'2014-07-03',51.44);
insert into venda values (642,11,5,'2014-08-14',23.14);
insert into venda values (2941,10,7,'2014-09-01',12.66);
insert into venda values (1292,5,9,'2014-05-02',321.01);
insert into venda values (361,4,1,'2014-01-20',73.44);
insert into venda values (2,11,4,'2014-02-14',3.14);
insert into venda values (191,15,1,'2014-03-10',62.66);
insert into venda values (122,5,2,'2014-04-22',31.64);
insert into venda values (51,5,5,'2014-05-21',183.99);
insert into venda values (62,4,4,'2014-06-24',29.44);
insert into venda values (371,11,4,'2014-09-23',82.66);
insert into venda values (1092,10,5,'2014-08-11',221.93);

insert into item_venda values (2,4,1,1,3.14);
insert into item_venda values (51,5,2,1,65.10);
insert into item_venda values (51,5,3,1,48.28);
insert into item_venda values (51,5,1,1,70.61);
insert into item_venda values (12941,5,31,1,28.49);
insert into item_venda values (12942,7,2,1,1921.72);
insert into item_venda values (2941,4,33,1,12.66);
insert into item_venda values (1292,5,47,1,245.61);
insert into item_venda values (1292,5,2,1,75.40);
insert into item_venda values (1092,5,47,1,221.93);
insert into item_venda values (642,4,1,8,2.50);
insert into item_venda values (642,5,50,1,3.14);
insert into item_venda values (541,5,36,1,51.44);
insert into item_venda values (442,5,31,2,19.39);
insert into item_venda values (442,4,4,1,19.36);
insert into item_venda values (441,5,1,1,123.44);
insert into item_venda values (371,5,36,1,82.66);
insert into item_venda values (361,4,31,10,5.80);
insert into item_venda values (361,4,41,1,15.44);
insert into item_venda values (191,5,36,1,62.66);
insert into item_venda values (122,4,1,10,2.50);
insert into item_venda values (122,5,50,1,6.64);
insert into item_venda values (62,4,1,1,2.50);
insert into item_venda values (62,4,31,1,5.80);
insert into item_venda values (62,4,41,1,1.78);
insert into item_venda values (62,5,50,1,5.33);
insert into item_venda values (62,4,33,1,14.03);