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
alter table goods drop column goods_name_eng;

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
select _, sell_price - buy_price as profit from goods
where sell_price-buy_price >=500;

select goods_name, goods_classify, sell_price from goods
where sell_price>=1000;

select goods_name, goods_classify, register_date from goods
where register_date <'2020-09-27';

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

-- 그룹화와 정렬

select goods_classify,count(\*) from goods group by goods_classify;

select buy_price, count(\*) from goods group by buy_price;

select goods_classify, avg(sell_price) from goods group by goods_classify;

select goods_classify, avg(sell_price) from goods
group by goods_classify
having avg(sell_price)>=2250;

-- 검색 결과 정리하기
select \* from goods
order by sell_price; -- 판매가격 기준 오름차순

select \* from goods
order by sell_price desc; -- 판매가격 기준 내림차순

-- 뷰 View
-- 뷰는 데이터가 아닌 쿼리를 저장하고 있다. 데이터가 없기에
-- 용량을 절약하며 자주 사용하는 쿼리를 매번 작성하지 않고 반복해서 사용 가능
create view GoodSum (goods_classify, cnt_goods)
as select goods_classify, count(\*) from goods
group by goods_classify;

select \* from GoodSum;

-- 뷰 삭제하기
drop view GoodSum;

-- 서브쿼리 SubQuery , 쿼리안의 쿼리
create view GoodSum ( goods_classify, cnt_goods )
as select goods_classify, count(\*) from goods
group by goods_classify;

select \* from GoodSum;

select goods_classify, cnt_goods
from (
select goods_classify, count(\*) as cnt_goods from goods
group by goods_classify
) as GoodsSum;

-- 스칼라 서브쿼리 , 단일 값이 반환하는 서브쿼리 , 비교연산자 가능
select avg(sell_price) from goods;

select \* from goods
where sell_price > (select avg(sell_price) from goods);

-- 스칼라 서브쿼리 : 평균 판매가격을 새로운 열로 만드는 쿼리
select goods_id, goods_name, sell_price, (select avg(sell_price) from goods) as avg_price from goods;

-- 스칼라 서브쿼리 : 상품 분류별 평균 판매가격이 전체 데이터의 평균 판매가격 이상인 데이터
select goods_classify, avg(sell_price) as avgPrice from goods
group by goods_classify
having avg(sell_price) > (select avg(sell_price) from goods);

-- 함수, 술어와 case식
-- 산술 함수는 숫자형 데이터의 절댓값, 오림, 내림,반올림 등을 계산할 수 있게 해준다.

create table SampleMath
(
m numeric (10,3),
n integer,
p integer
);

insert into SampleMath(m, n, p) values (500, 0, null);
insert into SampleMath(m, n, p) values (-180, 0, null);
insert into SampleMath(m, n, p) values (null, null, null);
insert into SampleMath(m, n, p) values (null, 7, 3);
insert into SampleMath(m, n, p) values (null, 5, 2);
insert into SampleMath(m, n, p) values (null, 4, null);
insert into SampleMath(m, n, p) values (8, null, 3);
insert into SampleMath(m, n, p) values (2.27, 1, null);
insert into SampleMath(m, n, p) values (5.555, 2, null);
insert into SampleMath(m, n, p) values (null, 1, null);
insert into SampleMath(m, n, p) values (8.76, null, null);

select \* from SampleMath;

-- abs : 절대값 계산
select m, abs(m) as abs_m from SampleMath;

-- mod : 나눗셈의 나머지 구하기
select n, p, mod(n, p) as mod_col from SampleMath;

-- round : 반올림하기. m의 값을 소수 n 자리까지 반올림하기
select m, n, round(m, n) as round_col from SampleMath;

-- 문자열 함수
create table SampleStr
(
str1 varchar(40),
str2 varchar(40),
str3 varchar(40)
);

select \* from SampleStr;

insert into SampleStr (str1, str2, str3) values('가나다', '라마', null);
insert into SampleStr (str1, str2, str3) values('abc', 'def', null);
insert into SampleStr (str1, str2, str3) values('김', '철수', '입니다');
insert into SampleStr (str1, str2, str3) values('aaa', null, null);
insert into SampleStr (str1, str2, str3) values(null, '가가가', null);
insert into SampleStr (str1, str2, str3) values('@#!@', null, null);
insert into SampleStr (str1, str2, str3) values('ABC', null, null);
insert into SampleStr (str1, str2, str3) values('aBC', null, null);
insert into SampleStr (str1, str2, str3) values('abc철수', 'abc', 'ABC');
insert into SampleStr (str1, str2, str3) values('abcabcabcdf', 'abc', 'ABC');
insert into SampleStr (str1, str2, str3) values('아이우', '이', '우');

-- concat : 문자열 연결
select str1, str2, concat(str1, str2) as str_concat from SampleStr;

-- lower : 소문자 변환
select str1, lower(str1) as low_str from SampleStr;

-- replace : 문자를 변경 ( 대상 문자열, 치환 전 문자열, 치환 후 문자열 )
select str1, str2, str3, replace(str1, str2, str3) as rep_str from SampleStr;

-- 날짜함수 : 현재 날짜, 시간, 일시
select current_date, current_time, current_timestamp;

-- 날짜 요소 추출하기
select
current_timestamp,
extract(year from current_timestamp) as year,
extract(month from current_timestamp) as month,
extract(day from current_timestamp) as day,
extract(hour from current_timestamp) as hour,
extract(minute from current_timestamp) as minute,
extract(second from current_timestamp) as second;

-- 술어 : 리턴값이 진리값(true,false,unKnown)인 함수 , like between, is null, insert
-- like : 문자열 부분 일치
create table SampleLike
(strcol varchar(6) not null,
primary key (strcol));

insert into SampleLike (strcol) values ('abcddd');
insert into SampleLike (strcol) values ('dddabc');
insert into SampleLike (strcol) values ('abdddc');
insert into SampleLike (strcol) values ('abcdd');
insert into SampleLike (strcol) values ('ddabc');
insert into SampleLike (strcol) values ('abddc');

-- like
select _ from SampleLike where strcol like 'ddd%'; -- ddd로 시작하는 모든 문자열
select _ from SampleLike where strcol like '%ddd%'; -- ddd가 포함된 모든 문자열
select \* from SampleLike where strcol like '%ddd'; -- 앞에 다른 문자가 있고 ddd가 후방에 위치

-- between
select \* from goods where sell_price between 100 and 1000;

-- is null, is not null, : null 데이터 선택
select _ from goods where buy_price is null; -- buy_price가 null인 열 선택
select _ from goods where buy_price is not null; -- buy_price가 null이 아닌 열 선택

-- in : 복수의 값을 지정
select \* from goods
where buy_price = 320
or buy_price = 500
or buy_price = 5000;

select _ from goods where buy_price in(320, 500, 5000);
select _ from goods where buy_price not in(320, 500, 5000);

-- case
select goods_name, sell_price,
case when sell_price >= 6000 then '고가'
when sell_price >= 3000 and sell_price< 6000 then '중가'
when sell_price < 3000 then '저가'
else null
end as price_classify
from goods;

-- 테이블과 집합과 결합

create table Goods2
(
goods_id char(4) not null,
goods_name varchar(100) not null,
goods_classify varchar(32) not null,
sell_price integer,
buy_price integer,
register_date date,
primary key (goods_id)
);

select \* from goods2;
insert into goods2 values ('0001', '티셔츠', '의류', 1000, 500, '2020-09-20');
insert into goods2 values ('0002', '펀칭기', '사무용품', 500, 320, '2020-09-11');
insert into goods2 values ('0003', '와이셔츠', '의류', 4000, 2800, null);
insert into goods2 values ('0004', '장갑', '의류', 800, 500, null);
insert into goods2 values ('0005', '주전자', '주방용품', 2000, 1700, '2020-09-20');

-- 테이블 행 합치기 : union , union all
select _ from goods union select _ from goods2; -- 001,002,003은 중복으로 중복행을 제외하고 합친다
select _ from goods union all select _ from goods2; -- 중복행 제외없이 모든 행을 합친다

-- 테이블 결합
create table StoreGoods
(
store_id char(4) not null,
store_name varchar(200) not null,
goods_id char(4) not null,
num integer not null,
primary key (store_id, goods_id)
);

insert into storegoods (store_id, store_name, goods_id, num) values ('000A', '서울', '0001', 30);
insert into storegoods (store_id, store_name, goods_id, num) values ('000A', '서울', '0002', 50);
insert into storegoods (store_id, store_name, goods_id, num) values ('000A', '서울', '0003', 15);
insert into storegoods (store_id, store_name, goods_id, num) values ('000B', '대전', '0002', 30);
insert into storegoods (store_id, store_name, goods_id, num) values ('000B', '대전', '0003', 120);
insert into storegoods (store_id, store_name, goods_id, num) values ('000B', '대전', '0004', 20);
insert into storegoods (store_id, store_name, goods_id, num) values ('000B', '대전', '0006', 10);
insert into storegoods (store_id, store_name, goods_id, num) values ('000B', '대전', '0007', 40);
insert into storegoods (store_id, store_name, goods_id, num) values ('000C', '부산', '0003', 20);
insert into storegoods (store_id, store_name, goods_id, num) values ('000C', '부산', '0004', 50);
insert into storegoods (store_id, store_name, goods_id, num) values ('000C', '부산', '0006', 90);
insert into storegoods (store_id, store_name, goods_id, num) values ('000C', '부산', '0007', 70);
insert into storegoods (store_id, store_name, goods_id, num) values ('000D', '대구', '0001', 100);

select \* from storegoods;

-- inner join : 내부 결합 goods_id를 기준으로 테이블의 결합
select store.store_id, store.store_name, store.goods_id,goods.goods_name, goods.sell_price
from StoreGoods as store
inner join Goods as goods
on store.goods_id = goods.goods_id;

-- outer join : 외부 결합 inner join은 두 테이블에 모두 존재하는 데이터를 합쳤지만 outer join 한쪽 테이블의 데이터도 합친다
select distinct(goods_id) from storegoods;
select distinct(goods_id) from goods;
select store.store_id, store.store_name,
goods.goods_id, goods.goods_name,goods.sell_price
from storegoods as store
right outer join goods as goods
on store.goods_id = goods.goods_id;

select store.store_id, store.store_name,
goods.goods_id, goods.goods_name,goods.sell_price
from storegoods as store
left outer join goods as goods
on store.goods_id = goods.goods_id;

-- 윈도우 함수
-- rank : partition by 순위를 정할 섹터 , order by 순서, rank() 순위 구하는 함수
select goods_name, goods_classify, sell_price,
rank() over (partition by goods_classify order by sell_price) as ranking
from goods;

select goods_name, goods_classify, sell_price,
rank() over (order by sell_price) as ranking
from goods;

-- rank : 복수행의 순위는 건너뛴다. dense_rank : 후순위를 건너뛰지 않는다. row_number : 순위와 상관없이 연속 번호를 부여
select goods_name, goods_classify, sell_price,
rank() over (order by sell_price) as ranking,
dense_rank() over (order by sell_price) as dense_ranking,
row_number() over (order by sell_price) as row_number_ranking
from goods;

-- 윈도우 함수에서 집약함수를 사용

-- 합계
select goods_id, goods_name, sell_price,
sum(sell_price) over() as current_sum
from goods;

-- 누적합계
select goods_id, goods_name, sell_price,
sum(sell_price) over(order by goods_id) as current_sum
from goods;

-- 누적평균
select goods_id, goods_name, sell_price,
avg(sell_price) over(order by goods_id) as current_avg
from goods;

-- 이동평균 계산하기
-- 최근 3개 데이터만 이용해서 이동평균을 계산하는 쿼리
-- rows n proceding을 입력하면 n 까지만 프레임을 만들어 계산한다. n=2는 앞에 2개까지만 계산하므로 3개의 평균을 계산하게 된다.
select goods_id, goods_classify, goods_name, sell_price,
avg(sell_price) over(order by goods_id rows 2 preceding) as moving_avg
from goods;

-- 뒤에 오는 2개의 데이터를 적용해서 이동평균을 계산하는 법
select goods_id, goods_classify, goods_name, sell_price,
avg(sell_price) over(order by goods_id rows between current row and 2 following) as moving_avg
from goods;

-- rows betweenn preceding and m following : n행과 뒤의 m행까지를 프레임으로 지정
-- 앞에1개 뒤에1개를 적용해 3개의 행을 이동평균계산
select goods_id, goods_classify, goods_name, sell_price,
avg(sell_price) over(order by goods_id
rows between 1 preceding and 1 following)
as moving_avg
from goods;
