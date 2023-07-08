# %%
import numpy as np
import pandas as pd
import matplotlib as plt
data_frame_1= pd.read_csv('D:\BTL_Python_data\VehicleJourney_Ecom_time(mai chuan).csv')
df1=data_frame_1.copy()
df1

# %%
df1.describe()

# %%
df1.shape

# %%
df1.info()

# %%
df1.isna().sum()

# %%
df1.loc[df1['supplierID'] == 'NaN']

# %%
data_frame_2= pd.read_csv('D:\BTL_Python_data\VehicleJourneyorderinfor.csv')
df2=data_frame_2.copy()
df2

# %%
df2.isna().sum()

# %%
df2[df2['DestinationLocation_Code'].isna()]
df2.drop(['DestinationLocation_Code', 'OriginLocation_Code'] , axis=1, inplace=True)
df2


# %%

df2.isna().sum()

# %%
df3= pd.concat([df1, df2], axis=1)
df3


# %%


# %%
df3=df3.drop(columns=['Make', 'Model'],axis=1)
df3.columns

# %%
df3

# %%
df3.isna().sum()

# %%


# %%
filt2=df3[df3['SENDERS_DATE'].isna()]
filt2.loc[filt2.order_id  == '3e292565d06','SENDERS_DATE']= '15/10/2015'
filt2.loc[filt2.order_id  == '3e292565d06','RECEIVERS_DATE']= '20/10/2015'
df3[df3['SENDERS_DATE'].isna()]=filt2
df3.isna().sum()

# %%
df3[df3['Material Shipped'].isna()]

# %%
data = pd.read_csv("D:\BTL_Python_data\Good_itemschuan.csv")
df4= data.copy()
df4

# %%
df4=df4.drop(index=df4.index[10005:50252])
df4

# %%
df54


# %%
df3=df3.drop('Material Shipped', axis=1)
df3=df3.join


