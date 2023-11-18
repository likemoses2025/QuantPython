# mysql 접속

mysql -u root -p

-- Create DataBase
create database shop;

-- use Database
use shop;

-- Create Table
create table goods(
goods_id char(4) not null,
goods_name varchar(100) not null,
goods_classify varchar(32) not null,
sell_price integer,
buy_price integer,
register_date date,
primary key (goods_id)
);

-- ADD column
alter table goods add column goods_name_eng varchar(100);

-- Delete column
alter table goods drop column goods_name_eng2;

-- 테이블에 데이터 등록하기
insert into goods values ('0001', '티셔츠', '의류',1000,500,'2020-09-20');
insert into goods values ('0002', '펀칭기', '사무용품',500,320,'2020-09-11');
insert into goods values ('0003', '와이셔츠', '의류',4000,2000,NULL);
insert into goods values ('0004', '식칼', '주방용품',3000,2000,'2020-09-20');
insert into goods values ('0005', '압력솥', '주방용품',6800,5000,'2020-01-15');
insert into goods values ('0006', '포크', '주방용품',500,NULL,'2020-09-20');
insert into goods values ('0007', '도마', '주방용품',880,790,'2020-04-28');
insert into goods values ('0008', '볼펜', '주방용품',100,null,'2020-11-11');

-- Select
select goods_id, goods_name, buy_price
from goods;

select \* from goods;

select goods_id as id, goods_name as name, buy_price as price from goods;

-- Select 계산식 작성하기
select '상품' as category, 38 as num, '2022-01-01' as date, goods_id, goods_name, sell_price, buy_price, sell_price - buy_price as profilt
from goods;

-- distinct : 중복 제거하기 ( 고유값만 가져오기 )
select distinct goods_classify from goods;

-- where 원하는 행 선택하기
select goods_name, goods_classify from goods where goods_classify="의류";

-- 연산자
select _, sell_price - buy_price as profit from goods;
select goods_name, sell_price - buy_price as profit from goods;
-- 이익이 500이상인 값들만 가져오기
select _, sell_price - buy_price as profit from goods where sell_price-buy_price >=500;

select goods_name, goods_classify, sell_price from goods where sell_price>=1000;

select goods_name, goods_classify, register_date from goods where register_date <'2020-09-27';

select goods_name, goods_classify, sell_price from goods
where goods_classify = "주방용품" and sell_price >= 3000;

select goods_name, goods_classify, sell_price from goods
where goods_classify = "주방용품" or sell_price >= 3000;

-- 집약함수 Count
select count(\*) from goods; -- 8행
select count(buy_price) from goods; -- 6행

-- 집약함수 SUM
select sum(sell_price), sum(buy_price) from goods;

-- 집약함수 avg
select avg(sell_price) from goods;

-- 집약함수 중복값 제외 후 집약함수 사용하기
select count(distinct goods_classify) from goods;
