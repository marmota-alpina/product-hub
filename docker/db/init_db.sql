drop table if exists products;
create table products
(
    id          CHAR(37)          not null primary key,
    source_id integer,
    source   varchar,
    title       varchar          not null,
    price       double precision not null,
    quantity    integer          not null default 0,
    description varchar,
    image       varchar,
    category    varchar,
    weight      double precision not null,
    length      double precision not null,
    width       double precision not null,
    height      double precision not null
);

DROP TABLE IF EXISTS configs;
CREATE TABLE configs
(
    id    VARCHAR(37) NOT NULL PRIMARY KEY,
    key   VARCHAR(30) NOT NULL,
    value VARCHAR(255) NOT NULL
);

CREATE UNIQUE INDEX config_key_uindex
    ON configs (key);

create unique index products_source_id_source_uindex
    on products (source_id, source);

alter table products
    owner to product_hub_user;