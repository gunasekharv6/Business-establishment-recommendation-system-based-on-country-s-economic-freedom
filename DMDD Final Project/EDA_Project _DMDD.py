#1
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import os

df = pd. read_csv("terror.csv")
df.columns

dff=df[["country_txt","region_txt","provstate","city","eventid","iyear","summary","attacktype1_txt","targtype1_txt","target1","gname","motive","weaptype1_txt","weapdetail","propextent_txt","propcomment"]]
dff=dff.sort_values(by=["country_txt"])

dff.isnull().values.any()
dff.isnull().sum()

dff.drop(['summary', 'motive'], axis=1,inplace=True)
dff.drop(['propcomment','propextent_txt'], axis=1,inplace=True)
dff.drop(['weapdetail'], axis=1,inplace=True)

dff.isnull().sum()

sns.pairplot(dff)
#plt.bar(df['eventid'], df['attacktype1_txt'], color ='maroon',width = 0.4)

#establishing sql connection
import mysql.connector

connection = mysql.connector.connect(host='localhost',
                                     user='root',
                                     password='SQLboston27!!')

mycursor = connection.cursor()

mycursor.execute("CREATE DATABASE yellow")  #Creating a database Ass3
#mycursor.execute("CREATE TABLE DMDD.global_terrorism(country varchar(150),region  varchar(150),state varchar(150),city varchar(150),attack_id integer,event_occured integer,attack_type varchar(500),target_type varchar(500),target varchar(500),attacked_by varchar(200),weapon_used varchar(200))")


from sqlalchemy import create_engine
import pymysql
engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}".format(host='localhost', db='yellow', user='root', pw='SQLboston27!!'))
dbconnection = engine.connect()
dff.to_sql('global_terrorism', engine, index=False)

#dff.to_excel("output1.xlsx")



#############################################
#2
#GDP_Growth

df = pd. read_csv("GDP.csv")
df.columns

df.isnull().values.any()
df.isnull().sum()

df.drop([0], inplace=True)

dff=df[["Country","2016","2017","2018","2019","2020","2021","2022"]]
dff=dff.sort_values(by=["Country"])

df.drop([230,229], inplace=True)

dff.isnull().values.any()
dff.isnull().sum()

dff.drop([216],inplace=True)
dff[['2016', '2017','2018','2019','2020','2021'] = dff[['2016', '2017','2018','2019','2020','2021']].apply(pd.to_numeric)
#sns.pairplot(dff)
#sns.violinplot(x=dff["2016"])
#sns.violinplot(data=df, x="Country", y="2016")

import mysql.connector

connection = mysql.connector.connect(host='localhost',
                                     user='root',
                                     password='SQLboston27!!')

mycursor = connection.cursor()
#mycursor.execute("CREATE TABLE Ass3.GDP_Growth(Country varchar(150),2016 float,2017 float,2018 float, 2019 float, 2020 float, 2021 float, 2022 float)")

from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}".format(host='localhost', db='yellow', user='root', pw='SQLboston27!!'))
dff.to_sql('GDP_Growth', engine, index=False)

#dff.to_excel("output2.xlsx")

##########################
#3
#climate
df = pd. read_csv("climate.csv")
df.columns

df.isnull().values.any()
df.isnull().sum()

dff=df[["rw_country_code","country","cri_rank","cri_score","losses_per_gdp__rank"]]
dff=dff.sort_values(by=["rw_country_code"])

#df.drop([230,229], inplace=True)

sns.pairplot(dff)
sns.violinplot(data=dff, x="rw_country_code", y="losses_per_gdp__rank", split=True)

import mysql.connector

connection = mysql.connector.connect(host='localhost',
                                     user='root',
                                     password='SQLboston27!!')

mycursor = connection.cursor()
#mycursor.execute("CREATE DATABASE ")  #Creating a database Ass3
#mycursor.execute("CREATE TABLE Ass3.global_climate(country_code varchar(150),country varchar(150),climaticcondition_rank integer,climatic_score integer, GDP_losses integer)")
from sqlalchemy import create_engine

import pandas as pymysql
engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}".format(host='localhost', db='yellow', user='root', pw='SQLboston27!!'))
dff.to_sql('global_climate', engine, index=False)

#dff.to_excel("output3.xlsx")

##################
#4
#Labor Cost

df = pd. read_csv("Laborcost.csv")
df.columns

df.drop([0,1,2,3], inplace=True)
df.columns = df.iloc[0]
df.drop([4], inplace=True)

#df.columns = df.iloc[0]

df.isnull().values.any()
df.isnull().sum()
df=df.dropna()
#dff=df[["rw_country_code","country","cri_rank","cri_score","losses_per_gdp__rank"]]
#dff=dff.sort_values(by=["rw_country_code"])

df['act1']=df.Economic_activity.str.split('.').str[1]
df['act2']=df.act1.str.split(';').str[0]

df.drop(['Source','Economic_activity','act1'], axis=1,inplace=True)
dff=df[['Reference area','Time','Local currency', '2017 PPP $', 'U.S. dollars', 'act2']]
dff=dff.dropna()
#sns.violinplot(x=dff["losses_per_gdp__rank"])
#sns.pairplot(dff)

import mysql.connector

connection = mysql.connector.connect(host='localhost',
                                     user='root',
                                     password='SQLboston27!!')



mycursor = connection.cursor()
#mycursor.execute("CREATE DATABASE ")  #Creating a database Ass3
#mycursor.execute("CREATE TABLE Ass3.Labor_Costs(country varchar(150),Time integer, Local_currency float, PPP$ float, wage_USD float, activity varchar(500))")

from sqlalchemy import create_engine

import pandas as pymysql
engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}".format(host='localhost', db='yellow', user='root', pw='SQLboston27!!'))
dff.to_sql('Labor_Costs', engine, index=False)

dff.to_excel("output4.xlsx")


##################
#5
#PPP
df = pd. read_csv("ppp.csv")
df.columns

df.drop(['SUBJECT','MEASURE','FREQUENCY','Flag Codes'], axis=1,inplace=True)

df.isnull().values.any()
df.isnull().sum()
df=df.dropna()
a=df.loc[df['TIME']==2010]

sns.pairplot(df)
sns.violinplot(data=df, x="TIME", y="Value")


import mysql.connector

connection = mysql.connector.connect(host='localhost',
                                     user='root',
                                     password='SQLboston27!!')



mycursor = connection.cursor()
#mycursor.execute("CREATE DATABASE ")  #Creating a database Ass3
#mycursor.execute("CREATE TABLE Ass3.PPP_value(country varchar(150),INDICATOR varchar(150), TIME integer, PPP_Value float)")

from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}".format(host='localhost', db='yellow', user='root', pw='SQLboston27!!'))
df.to_sql('PPP_value', engine, index=False)

#df.to_excel("output5.xlsx")


##################################
#6
#Forbes

df = pd. read_csv("Forbes.csv")
df.columns

df.isnull().values.any()
df.isnull().sum()
df=df.dropna()

sns.pairplot(df)
#plot = df.plot.pie(subplots=True, figsize=(11, 6))

import mysql.connector

connection = mysql.connector.connect(host='localhost',
                                     user='root',
                                     password='SQLboston27!!')

mycursor = connection.cursor()

#mycursor.execute("CREATE TABLE DMDD.Forbes_Data(Ranking integer, Company varchar(150), Country varchar(150), Sales Float, Profits_USD Float, Assets Float, Market_value Float, Sector varchar(500), Industry varchar(500))")

from sqlalchemy import create_engine


import pymysql
engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}".format(host='localhost', db='yellow', user='root', pw='SQLboston27!!'))
dbconnection = engine.connect()
df.to_sql('Forbes_Data', engine, index=False)

df.to_excel("output6.xlsx")


#############
#7
#inward_remittance
df = pd. read_excel("outward_remittance.xlsx")
df.columns

df.drop(df.iloc[:,1:27], axis=1, inplace=True)

df.isnull().values.any()
df.isnull().sum()

df=df.dropna()


sns.pairplot(df)

import mysql.connector

connection = mysql.connector.connect(host='localhost',
                                     user='root',
                                     password='SQLboston27!!')

mycursor = connection.cursor()

#mycursor.execute("CREATE TABLE DMDD.Forbes_Data(Ranking integer, Company varchar(150), Country varchar(150), Sales Float, Profits_USD Float, Assets Float, Market_value Float, Sector varchar(500), Industry varchar(500))")


from sqlalchemy import create_engine


import pymysql
engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}".format(host='localhost', db='yellow', user='root', pw='SQLboston27!!'))
dbconnection = engine.connect()
df.to_sql('inward_remittance', engine, index=False)

#df.to_excel("output7.xlsx")


############
#8
#efw
df = pd. read_excel("efotw-2022-master-index-data-for-researchers-iso.xlsx")
df.columns

df.drop([0,1,2], inplace=True)
df.columns = df.iloc[0]
df.drop([3],inplace=True)

df.isnull().values.any()
df.isnull().sum()

dff=df[['Year','ISO Code 3', 'Countries','Region', 'World Bank Region']]

dff.isnull().values.any()
dff.isnull().sum()

sns.pairplot(dff)

#establishing sql connection
#pip install mysql-connector-python
import mysql.connector

connection = mysql.connector.connect(host='localhost',
                                     user='root',
                                     password='SQLboston27!!')

#mycursor = connection.cursor()

#mycursor.execute("CREATE TABLE DMDD.Forbes_Data(Ranking integer, Company varchar(150), Country varchar(150), Sales Float, Profits_USD Float, Assets Float, Market_value Float, Sector varchar(500), Industry varchar(500))")


from sqlalchemy import create_engine
import pymysql
engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}".format(host='localhost', db='yellow', user='root', pw='SQLboston27!!'))
dbconnection = engine.connect()
dff.to_sql('efw', engine, index=False)

#df.to_excel("output8.xlsx")

####################################
#9
#outward_reittance

df = pd. read_excel("outward_remittance.xlsx")
df.columns

df.columns = df.iloc[0]
df.drop([0], inplace=True)

df.drop(df.iloc[:,1:27], axis=1, inplace=True)

df.isnull().values.any()
df.isnull().sum()

df=df.dropna()


sns.pairplot(df)

#establishing sql connection
#pip install mysql-connector-python
import mysql.connector

connection = mysql.connector.connect(host='localhost',
                                     user='root',
                                     password='SQLboston27!!')

mycursor = connection.cursor()

#mycursor.execute("CREATE TABLE DMDD.Forbes_Data(Ranking integer, Company varchar(150), Country varchar(150), Sales Float, Profits_USD Float, Assets Float, Market_value Float, Sector varchar(500), Industry varchar(500))")

from sqlalchemy import create_engine
import pymysql
engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}".format(host='localhost', db='yellow', user='root', pw='SQLboston27!!'))
dbconnection = engine.connect()
df.to_sql('outward_remittance', engine, index=False)

#df.to_excel("output9.xlsx")


############################
#10
#economic_factors
df = pd. read_excel("economic_factors.xlsx")
df.columns

df.columns = df.iloc[0]
df.drop([0], inplace=True)

df.isnull().values.any()
df.isnull().sum()

#df.hist(column='session_duration_seconds')
sns.pairplot(df)

import mysql.connector

connection = mysql.connector.connect(host='localhost',
                                     user='root',
                                     password='SQLboston27!!')

mycursor = connection.cursor()

#mycursor.execute("CREATE TABLE DMDD.Forbes_Data(Ranking integer, Company varchar(150), Country varchar(150), Sales Float, Profits_USD Float, Assets Float, Market_value Float, Sector varchar(500), Industry varchar(500))")


from sqlalchemy import create_engine


import pymysql
engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}".format(host='localhost', db='yellow', user='root', pw='SQLboston27!!'))
dbconnection = engine.connect()
df.to_sql('economic_factors', engine, index=False)

#df.to_excel("output10.xlsx")


#######
#forex
df = pd. read_excel("ForexReserves.xlsx")
df.columns

df.isnull().values.any()
df.isnull().sum()

df=df.dropna()
#df2 = df.rename({'a': 'X', 'b': 'Y'}, axis=1)

sns.pairplot(df)
#df.boxplot(by ='Countries', column ='Reserves, 2021', grid = False)
#df['Reserves, 2021'] = df['Reserves, 2021'].astype(float)

import mysql.connector

connection = mysql.connector.connect(host='localhost',
                                     user='root',
                                     password='SQLboston27!!')

mycursor = connection.cursor()

#mycursor.execute("CREATE TABLE DMDD.Forbes_Data(Ranking integer, Company varchar(150), Country varchar(150), Sales Float, Profits_USD Float, Assets Float, Market_value Float, Sector varchar(500), Industry varchar(500))")


from sqlalchemy import create_engine
import pymysql
engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}".format(host='localhost', db='yellow', user='root', pw='SQLboston27!!'))
dbconnection = engine.connect()
df.to_sql('Forex_Reserves', engine, index=False)


