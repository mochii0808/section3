CREATE TABLE Customer(
    customer_id INTEGER NOT NULL,
    #필드명 / 데이터 타입 / 규제조건
    customer_name VARCHAR(32) NOT NULL,
    #    / 데이터 타입(데이터 크기)/
    customer_age INTEGER,
    PRIMARY KEY(customer_id)
);  #키 지정


CREATE TABLE Customer(
    customer_id INTEGER NOT NULL PRIMARY KEY,
    #                           키 지정 방법 2
    customer_name VARCHAR(32) NOT NULL,
    customer_age INTEGER,
);


CREATE TABLE Customer(
    customer_id INTEGER NOT NULL,
    customer_name VARCHAR(32) NOT NULL,
    customer_age INTEGER,
    PRIMARY KEY(customer_id, customer_name)
);  #다중 키 지정
