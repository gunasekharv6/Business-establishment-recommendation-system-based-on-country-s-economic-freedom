drop database DMDD;

Select * from yellow.forbes_data;

#usecase 1
#Find country with particular sector and get the GDP rank associated with it
SELECT * from(
(select * from yellow.forbes_data
where Company in ('JPMorgan Chase', 'Agricultural Bank of China', 'Charles Schwab') )A
Inner Join
(select * from yellow.gdp_growth)B
on A.`Country/Territory`=B.Country) ;



#usecase 2
SELECT * from(
(select * from yellow.global_climate
where cri_rank=63)A
Inner Join
(select LOCATION, Value from yellow.ppp_value)B
on A.rw_country_code=B.LOCATION) LIMIT 1;

#usecase 3
#Find countries with Financial sector and their associated Forex Reserves
SELECT *  from(
(select * from yellow.forbes_data
where Sector in ('Health Care', 'Financials', 'Materials'))A
Inner Join
(select * from yellow.Forex_Reserves)B
on A.`Country/Territory`=B.Countries ) ;

#usecase 4
#Find countries with cri_rank more than 130 and their associated profits with sector
SELECT A.country, A.cri_rank, B.Company, B.Sector, B.Industry, B.Sales, B.Profits from(
(select * from yellow.global_climate
where cri_rank>130)A
Inner Join
(select `Country/Territory`,Company, Sector, Industry, Sales, Profits from yellow.forbes_data)B
on A.country=B.`Country/Territory`);

select * from yellow.ppp_value;
#usecase 5
#Find companies with rank less than 20 with associated PPP, dollars and sector
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
#Find country named United States and itsGDP growth 
Select *  from(
(select * from yellow.gdp_growth)A
Inner join
(select `Country/Territory`,Company, Sector, Industry, Sales, Profits from yellow.forbes_data)B
On A.Country= B.`Country/Territory`)
Where Sector='Energy';


select * from yellow.outward_remittance;
#usecase 7
#Find countries with sales more than $150B with profits greater than $10B get remittance 

select * from(
(select `Country/Territory`,Company, Sector, Industry, Sales, Profits from yellow.forbes_data
where Profits>'$10B')A
Inner Join
(select * from yellow.outward_remittance)B
on A.`Country/Territory` = B.`Outward remittance flows (US$ million)`);


#usecase 8
#Find country named Japan get freedom to trade internationally their companies and market value of same
select * from(
(select `Country/Territory`,Company, Sector, Industry, Sales, Profits from yellow.forbes_data
where Profits>'$10B'
and Industry in ('Regional Banks', 'Recreational Products'))A
Inner Join
(select * from yellow.labor_costs)B
on A.`Country/Territory` = B.`Reference area`);

#usecase 9
#Find countries with financial sector with assets and associated legal systems and property rights with companies
select * from(
(select `Country/Territory`,Company, Sector, Industry, Sales, Profits from yellow.forbes_data
where Profits>'$10B'
and Industry in ('Regional Banks', 'Recreational Products'))A
Inner Join
(select * from yellow.economic_factors)B
on A.`Country/Territory` = B.`COUNTRY NAME `);

#usecase 10
#Find countries with sound money more than 1.4 and profits of the companies in the associated country
select * from(
(select `Country/Territory`,Company, Sector, Industry, Sales, Profits from yellow.forbes_data
where Profits>'$1.3B')A
Inner Join
(select * from yellow.economic_factors
where REGULATION >=8.3)B
on A.`Country/Territory` = B.`COUNTRY NAME `);


#usecase 11
#Find country named India with outward remittance flow and companies in the country with government size
select * from(
(select * from yellow.outward_remittance)A
Inner Join
(select * from yellow.economic_factors
where REGULATION >=8.3)B
on A.`Outward remittance flows (US$ million)` = B.`COUNTRY NAME `);

#usecase 12
#Find country named Canada and find PPP for the country and get associated international trade, regulations 
#with profits made in which industry sector

SELECT Distinct A.country, A.cri_score, A.losses_per_gdp__rank from(
(select * from yellow.global_climate
where cri_score>=43.2)A
Inner Join
(select LOCATION, Value from yellow.ppp_value)B
on A.rw_country_code=B.LOCATION);


#usecase 13
#Find countries with PPP value greater than 1 and year greater than 2000 with the sector, 
#company and industry parameters associated with that country 

SELECT * from(
(select * from yellow.forbes_data)A
Inner Join
(select * from yellow.efw)B
on A.`Country/Territory`=B.Countries);

#usecase 14
#Find countries with local currency greater than 5 with associated industry, company and sector

SELECT * from(
(select * from yellow.forbes_data)A
Inner Join
(select * from yellow.labor_costs
where `Local currency`>5)B
on A.`Country/Territory`=B.`Reference area`);

#usecase 15
#Find country named Italy and company, sector and industry with profits, 
#legal systems & property rights associated with it

SELECT * from(
(select * from yellow.forbes_data)A
Inner Join
(select * from yellow.economic_factors)B
on A.`Country/Territory`=B.`COUNTRY NAME `)
Where `Country/Territory` = 'Italy';

#usecase 16

SELECT * from(
(select * from yellow.forex_reserves)A
Inner Join
(select * from yellow.gdp_growth)B
on A.`Countries `=B.Country)
order by A.`Global rank ` LIMIT 1;

#usecase 17
#Select the country with max inward remittance in 2021 and their gdp
SELECT * from(
(select * from yellow.outward_remittance)A
Inner Join
(select * from yellow.gdp_growth)B
on A.`Outward remittance flows (US$ million)`=B.Country)
order by B.`2022` Desc Limit 10 ;

#usecase18
#View the country with top 10 gdp in 2021 and their corresponding forex reserves
SELECT * from(
(select * from yellow.forex_reserves)A
Inner Join
(select * from yellow.gdp_growth)B
on A.`Countries `=B.Country)
WHERE B.Country in ('China', 'India', 'France', 'Germany')
order by B.`2022` DESC LIMIT 5;


#usecase 19
#User makes a search for country with lowest labor cost along with their gdp
SELECT * from(
(select * from yellow.labor_costs)A
Inner Join
(select * from yellow.gdp_growth)B
on A.`Reference area`=B.Country)
order by A.`U.S. dollars` LIMIT 1;

#usecase 20
#
SELECT * from(
(select country_txt,Count(eventid) Total_attacks from yellow.global_terrorism
group by country_txt)A
Inner Join
(select * from yellow.gdp_growth)B
on A.country_txt=B.Country)
order by Total_attacks Desc;







 










