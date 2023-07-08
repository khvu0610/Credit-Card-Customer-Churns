# %%
import pandas as pd
import numpy as np
%matplotlib inline
import matplotlib.pyplot as plt

# %%
data = pd.read_csv("D:\Filechuan\dataset\Europe_supply_chain.csv")
df = data.copy()
df

# %%
df.info()

# %%
data1 = pd.read_csv("D:\Filechuan\dataset\FleetJourneyorderinfor.csv")
df1 = data1.copy()
df1

# %%
df1=df1.drop(index=df1.index[10000:10006])
df1

# %%
df2= pd.concat([df1,df['Customer Fname'] ,df['Customer Lname'],df['Order City'],df['Order Country'],df['Order Item Cardprod Id'],df['Product Name'],df['Order Item Discount'],df['Order Item Discount Rate'],df['Order Item Id'],df['Order Item Quantity'],df['Order Item Product Price'],df['Order Item Profit Ratio'],df['Sales'],df['Order Item Total'],df['Order Profit Per Order'],df['Order Region'],df['Order State'],df['Order Status']], axis=1)
df2

# %%
df2=df2.drop(index=df2.index[10000:50252])
df2

# %%
df2 = df2.drop('Unnamed: 8', axis=1)
df2 = df2.drop('PLACE_OF_RECEIVERS 1', axis=1)
df2 = df2.drop('PLACE_OF_RECEIVERS 2', axis=1)
df2 = df2.drop('PLACE_OF_RECEIVERS 3', axis=1)

# %%
df2["Customer Name"] = df2[["Customer Fname", "Customer Lname"]].apply("-".join, axis=1)

# %%
df2.isna().sum()

# %%
df2['order_id_date'] = pd.to_datetime(df2['order_id_date'])

# %%
df2.to_csv(r"D:\Filechuan\New\Order.csv", index=False)



