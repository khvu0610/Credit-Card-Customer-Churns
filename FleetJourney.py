# %%
import numpy as np
import pandas as pd
import matplotlib as plt
data_frame_1= pd.read_csv('D:\BTL_Python_data\FleetJourney_EcomUStime.csv')
df1=data_frame_1.copy()
df1

# %%
df1.describe()

# %%
df1.shape

# %%
df1.info()

# %%
data_frame_2= pd.read_csv('D:\BTL_Python_data\FleetJourneyorderinfor.csv')
df2=data_frame_2.copy()
df2

# %%
df3= pd.concat([df1, df2], axis=1)
df3

# %%
df3.isna().sum()

# %%
filt1=df3[df3['SENDERS_DATE'].isna()]
filt1

# %%
filt1.loc[filt1.order_id == '99e25010475','SENDERS_DATE']= '06/09/2021'
filt1.loc[filt1.order_id == '99e25010475','RECEIVERS_DATE']= '15/09/2021'
filt1
df3[df3['SENDERS_DATE'].isna()]=filt1

# %%
df3.isna().sum()

# %%
df4=pd.read_csv('D:\BTL_Python_data\Adult.csv', dtype='unicode')
df4

# %%
df3=df3.join(df4['Customer Fname'])
df3=df3.join(df4['Customer Lname'])
df3

# %%
df3=df3.drop('First_name', axis=1)
df3


