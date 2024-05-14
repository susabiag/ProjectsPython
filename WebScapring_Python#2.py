
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 12:42:08 2022

@author: santi
"""

import datetime as dt
import pandas as pd

#--------------------------Beef----------------------------------------------------------------------------
filepath ='C:\\Users\\Santi\\Downloads\\'
filecsv = 'beef.csv'

#File organized csv
fileorgcsv = 'beef_cleaned.csv'

#bf is equal to beef file csv
bf = pd.read_csv(r"C:\\Users\\santi\\Downloads\\beef.csv")
bf



#dropping unecessary columns
bf.drop(bf.columns[0],axis=1,inplace=True)
bf.drop(bf.columns[1],axis=1,inplace=True)
bf.drop(bf.columns[2],axis=1,inplace=True)


#Renaming columns
bf.rename(columns={'Choice beef values and spreads and the all-fresh retail value': 'Date'}, inplace=True)
bf.rename(columns={'Unnamed: 2': 'RetailValue'}, inplace=True)
bf.rename(columns={'Unnamed: 3': 'WholesaleValue'}, inplace=True)
bf.rename(columns={'Unnamed: 4': 'GrossFarmValue'}, inplace=True)
bf.rename(columns={'Unnamed: 5': 'ByProductAllowance'}, inplace=True)
bf.rename(columns={'Unnamed: 6': 'NetFarmValue'}, inplace=True)
bf.rename(columns={'Unnamed: 7': 'Total'}, inplace=True)
bf.rename(columns={'Unnamed: 8': 'WholesaleToRetail'}, inplace=True)
bf.rename(columns={'Last update': 'FarmToWholesale'}, inplace=True)
bf.rename(columns={'Unnamed: 10': 'FarmersShare'}, inplace=True)
bf.rename(columns={'Next update': '5MarketSteerPrice'}, inplace=True)
bf.rename(columns={'Unnamed: 12': 'All-FreshBeefRetailValue'}, inplace=True)

#Droping unecessary rows
bf.drop(bf.index[49:],inplace=True)
bf.drop(bf.index[0:28],inplace=True)


bf['Time'] = pd.to_datetime(bf['Date'])
bf['Year'] = pd.to_datetime(bf['Date']).dt.year
bf['Month'] = pd.to_datetime(bf['Date']).dt.month

#Dropping one column more bf
bf.drop(bf.columns[11],axis=1,inplace=True)


#Making values as int

bf['RetailValue'] = bf['RetailValue'].astype(float)
bf['GrossFarmValue'] = bf['GrossFarmValue'].astype(float)
bf['ByProductAllowance'] = bf['ByProductAllowance'].astype(float)
bf['NetFarmValue'] = bf['NetFarmValue'].astype(float)
bf['Total'] = bf['Total'].astype(float)
bf['WholesaleToRetail'] = bf['WholesaleToRetail'].astype(float)
bf['FarmToWholesale'] = bf['FarmToWholesale'].astype(float)
bf['FarmersShare'] = bf['FarmersShare'].astype(float)
bf['5MarketSteerPrice'] = bf['5MarketSteerPrice'].astype(float)
bf['All-FreshBeefRetailValue'] = bf['All-FreshBeefRetailValue'].astype(float)




#------------------------------------------------Energy---------------------------------------------------
fileoriginalE = 'C:\\Users\santi\Downloads\EnergyP.xls'


df1 = pd.DataFrame(pd.read_excel(fileoriginalE,'Data 1'))

#Eliminando columnas
#df.drop(df.columns[0],axis=1,inplace=True)

#Eliminate rows

df1.drop(df1.index[0:335],inplace=True)


#Changing column names
df1.rename(columns={'Back to Contents': 'Date'}, inplace=True)
df1.rename(columns={'Data 1: U.S. All Grades All Formulations Retail Gasoline Prices (Dollars per Gallon)': 'GasolinePricesDollarsPerGallon'}, inplace=True)



#df['Day'] = pd.to_datetime(df['Date']).dt.day

df1['Year'] = pd.to_datetime(df1['Date']).dt.year
df1['Month'] = pd.to_datetime(df1['Date']).dt.month

df1.drop(df1.columns[0],axis=1,inplace=True)

#Changing into to float
df1['GasolinePricesDollarsPerGallon'] = df1['GasolinePricesDollarsPerGallon'].astype(float)




#---------------------------------------------Inflation-------------------------------------------------------
fileoriginal ='C:\\Users\\Santi\\Downloads\\statistic_id273418_us-monthly-inflation-rate-september-2022.xlsx'


df = pd.DataFrame(pd.read_excel(fileoriginal,'Data'))
#Eliminando columnas
df.drop(df.columns[0],axis=1,inplace=True)

#Dropping rows
df.drop(df.index[0:16],inplace=True)

#Changing column names
df.rename(columns={'Unnamed: 1': 'Date'}, inplace=True)
df.rename(columns={'Unnamed: 2': 'Percentage'}, inplace=True)
df.rename(columns={'Unnamed: 3': 'Metric'}, inplace=True)

#Changing row values
df.loc[16,'Date']='2021-01'
df.loc[17,'Date']='2021-02'
df.loc[18,'Date']='2021-03'
df.loc[19,'Date']='2021-04'
df.loc[20,'Date']='2021-05'
df.loc[21,'Date']='2021-06'
df.loc[22,'Date']='2021-07'
df.loc[23,'Date']='2021-08'
df.loc[24,'Date']='2021-09'
df.loc[25,'Date']='2021-10'
df.loc[26,'Date']='2021-11'
df.loc[27,'Date']='2021-12'
df.loc[28,'Date']='2022-01'
df.loc[29,'Date']='2022-02'
df.loc[30,'Date']='2022-03'
df.loc[31,'Date']='2022-04'
df.loc[32,'Date']='2022-05'
df.loc[33,'Date']='2022-06'
df.loc[34,'Date']='2022-07'
df.loc[35,'Date']='2022-08'
df.loc[36,'Date']='2022-09'


#Changing column names
df.rename(columns={'Unnamed: 1': 'Date'}, inplace=True)
df.rename(columns={'Unnamed: 2': 'Percentage'}, inplace=True)
df.rename(columns={'Unnamed: 3': 'Metric'}, inplace=True)


df['Month'] = pd.to_datetime(df['Date']).dt.month
df['Year'] = pd.to_datetime(df['Date']).dt.year
df['Time'] = pd.to_datetime(df['Date'])

df['Percentage'] = df['Percentage']/100

#Dropping extra columns
df.drop(df.columns[0],axis=1,inplace=True)
df.drop(df.columns[4],axis=1,inplace=True)





#---------------------------------------------------------Merging---------------------------------
bf = bf.merge(df,how='inner',on=['Month','Year'])
df_official = bf.merge(df1,how='inner',on=['Month','Year'])
filecsvFinal = 'MergedData.csv'
fileFinal = df_official.to_csv(filepath+filecsvFinal,sep=',')
fileFinal

#--------------------------------------------------------Adding columns---------------------------
#Taking off inflation beef
df_official['RetailValueBeefInflation'] = df_official['RetailValue'] * df_official['Percentage'] 
df_official['RetailValueBeefNoInflation'] = df_official['RetailValue'] - df_official['RetailValueBeefInflation']

df_official['TotalBeefInflation'] = df_official['Total'] * df_official['Percentage'] 
df_official['TotalBeefNoInflation'] = df_official['Total'] - df_official['TotalBeefInflation']

df_official['All-FreshBeefRetailValue_Inflation'] = df_official['All-FreshBeefRetailValue'] * df_official['Percentage'] 
df_official['All-FreshBeefRetailValue_NoInflation'] = df_official['All-FreshBeefRetailValue'] - df_official['All-FreshBeefRetailValue_Inflation']

#Taking off inflation on 'Gasoline Prices Dollars Per Gallon'
df_official['GasolinePricesDollarsPerGallon_Inflation'] = df_official['GasolinePricesDollarsPerGallon'] * df_official['Percentage'] 
df_official['GasolinePricesDollarsPerGallon_NoInflation'] = df_official['GasolinePricesDollarsPerGallon'] - df_official['GasolinePricesDollarsPerGallon_Inflation']
