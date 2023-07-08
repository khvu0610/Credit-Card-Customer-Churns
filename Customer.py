# %%
import pandas as pd
import numpy as np
%matplotlib inline
import matplotlib.pyplot as plt

# %%
data1 = pd.read_csv("D:/Filechuan/adult.csv")
df1 = data1.copy()
df1

# %%
df1.drop(['fnlwgt'],axis=1,inplace=True)

# %%
df1.info()

# %%
data2 = pd.read_csv("D:\Filechuan\dataset\Europe_supply_chain.csv")
df2 = data2.copy()
df2

# %%
data69 = pd.read_csv("D:\Filechuan\dataset\FleetJourney_EcomUStime.csv")
df69= data69.copy()
df69

# %%
df3 = pd.concat([df1, df2['Customer City'], df69['customer_id'],df2['Customer Fname'],df2['Customer Lname'],df2['Customer Email'],df2['Customer Password'],df2['Order City'],df2['Order State'],df2['Order Region']],axis=1)
df3


# %%
data = pd.read_csv("D:\Filechuan\dataset\FleetJourneyorderinfor.csv")
df = data.copy()
df

# %%
df4 = pd.concat([df3, df['PLACE_OF_RECEIVERS 1']],axis=1)
df4

# %%
df4=df4.drop(index=df4.index[10006:50252])

# %%
df4.isna().sum()

# %%
df4 = df4.dropna()


# %%
df4['workclass'] = df4['workclass'].replace('?', 'Private')
df4['occupation'] = df4['occupation'].replace('?', 'Prof-specialty')
df4['native.country'] = df4['native.country'].replace('?', 'United-States')
df4

# %%
df4.to_csv(r"D:\Filechuan\New\Customer.csv", index=False)



