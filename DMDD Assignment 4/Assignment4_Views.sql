 #usecase 1
CREATE VIEW  yellow.view1 AS
SELECT * from(
(select * from yellow.forbes_data
where Company in ('JPMorgan Chase', 'Agricultural Bank of China', 'Charles Schwab') )A
Inner Join
(select * from yellow.gdp_growth)B
on A.`Country/Territory`=B.Country) ;



#usecase 2
CREATE VIEW yellow.view2 AS
SELECT * from(
(select * from yellow.global_climate
where cri_rank=63)A
Inner Join
(select LOCATION, Value from yellow.ppp_value)B
on A.rw_country_code=B.LOCATION) LIMIT 1;

#usecase 3
CREATE VIEW yellow.view3 AS
SELECT *  from(
(select * from yellow.forbes_data
where Sector in ('Health Care', 'Financials', 'Materials'))A
Inner Join
(select * from yellow.Forex_Reserves)B
on A.`Country/Territory`=B.Countries ) ;

#usecase 4
CREATE VIEW yellow.view4 AS
SELECT A.country, A.cri_rank, B.Company, B.Sector, B.Industry, B.Sales, B.Profits from(
(select * from yellow.global_climate
where cri_rank>130)A
Inner Join
(select `Country/Territory`,Company, Sector, Industry, Sales, Profits from yellow.forbes_data)B
on A.country=B.`Country/Territory`);

#usecase 5
CREATE VIEW yellow.view5 AS
Select * from
(SELECT country, Value from(
(select rw_country_code, country from yellow.global_climate)A
Inner Join
(select LOCATION, Value from yellow.ppp_value)B
on A.rw_country_code=B.LOCATION))C
Inner Join
(select * from yellow.forbes_data
where `Rank`<50)D
On C.country=D.`Country/Territory`;

#usecase 6
CREATE VIEW yellow.view6 AS
Select *  from(
(select * from yellow.gdp_growth)A
Inner join
(select `Country/Territory`,Company, Sector, Industry, Sales, Profits from yellow.forbes_data)B
On A.Country= B.`Country/Territory`)
Where Sector='Energy';

#usecase 7
CREATE VIEW yellow.view7 AS
select * from(
(select `Country/Territory`,Company, Sector, Industry, Sales, Profits from yellow.forbes_data
where Profits>'$10B')A
Inner Join
(select * from yellow.outward_remittance)B
on A.`Country/Territory` = B.`Outward remittance flows (US$ million)`);


#usecase 8
CREATE VIEW yellow.view8 AS
select * from(
(select `Country/Territory`,Company, Sector, Industry, Sales, Profits from yellow.forbes_data
where Profits>'$10B'
and Industry in ('Regional Banks', 'Recreational Products'))A
Inner Join
(select * from yellow.labor_costs)B
on A.`Country/Territory` = B.`Reference area`);

#usecase 9
CREATE VIEW yellow.view9 AS
select * from(
(select `Country/Territory`,Company, Sector, Industry, Sales, Profits from yellow.forbes_data
where Profits>'$10B'
and Industry in ('Regional Banks', 'Recreational Products'))A
Inner Join
(select * from yellow.economic_factors)B
on A.`Country/Territory` = B.`COUNTRY NAME `);

#usecase 10
CREATE VIEW yellow.view10 AS
select * from(
(select `Country/Territory`,Company, Sector, Industry, Sales, Profits from yellow.forbes_data
where Profits>'$1.3B')A
Inner Join
(select * from yellow.economic_factors
where REGULATION >=8.3)B
on A.`Country/Territory` = B.`COUNTRY NAME `);


#usecase 11
CREATE VIEW yellow.view11 AS
select * from(
(select * from yellow.outward_remittance)A
Inner Join
(select * from yellow.economic_factors
where REGULATION >=8.3)B
on A.`Outward remittance flows (US$ million)` = B.`COUNTRY NAME `);

#usecase 12
CREATE VIEW yellow.view12 AS
SELECT Distinct A.country, A.cri_score, A.losses_per_gdp__rank from(
(select * from yellow.global_climate
where cri_score>=43.2)A
Inner Join
(select LOCATION, Value from yellow.ppp_value)B
on A.rw_country_code=B.LOCATION);


#usecase 13
CREATE VIEW yellow.view13 AS
SELECT * from(
(select * from yellow.forbes_data)A
Inner Join
(select * from yellow.efw)B
on A.`Country/Territory`=B.Countries);

#usecase 14
CREATE VIEW yellow.view14 AS
SELECT * from(
(select * from yellow.forbes_data)A
Inner Join
(select * from yellow.labor_costs
where `Local currency`>5)B
on A.`Country/Territory`=B.`Reference area`);

#usecase 15
CREATE VIEW yellow.view15 AS
SELECT * from(
(select * from yellow.forbes_data)A
Inner Join
(select * from yellow.economic_factors)B
on A.`Country/Territory`=B.`COUNTRY NAME `)
Where `Country/Territory` = 'Italy';


#usecase 16
CREATE VIEW yellow.view16 AS
SELECT * from(
(select * from yellow.forex_reserves)A
Inner Join
(select * from yellow.gdp_growth)B
on A.`Countries `=B.Country)
order by A.`Global rank ` LIMIT 1;

#usecase 17
CREATE VIEW yellow.view17 AS
SELECT * from(
(select * from yellow.outward_remittance)A
Inner Join
(select * from yellow.gdp_growth)B
on A.`Outward remittance flows (US$ million)`=B.Country)
order by B.`2022` Desc Limit 10 ;

#usecase18
CREATE VIEW yellow.view18 AS
SELECT * from(
(select * from yellow.forex_reserves)A
Inner Join
(select * from yellow.gdp_growth)B
on A.`Countries `=B.Country)
WHERE B.Country in ('China', 'India', 'France', 'Germany')
order by B.`2022` DESC LIMIT 5;


#usecase 19
CREATE VIEW yellow.view19 AS
SELECT * from(
(select * from yellow.labor_costs)A
Inner Join
(select * from yellow.gdp_growth)B
on A.`Reference area`=B.Country)
order by A.`U.S. dollars` LIMIT 1;

#usecase 20
CREATE VIEW yellow.view20 AS
SELECT * from(
(select country_txt,Count(eventid) Total_attacks from yellow.global_terrorism
group by country_txt)A
Inner Join
(select * from yellow.gdp_growth)B
on A.country_txt=B.Country)
order by Total_attacks Desc;

