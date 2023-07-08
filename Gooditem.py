# %%
import pandas as pd
import numpy as np
%matplotlib inline
import matplotlib.pyplot as plt

# %%
data = pd.read_csv("D:\Filechuan\Good_itemschuan.csv")
df = data.copy()
df

# %%
df=df.drop(index=df.index[12000:50252])

# %%
df

# %%
df.drop(['Product Description'],axis=1,inplace=True)

# %%
df.isna().sum()

# %%
df = df.dropna()
df

# %%
data1 = pd.read_csv("D:\Filechuan\delivery_orderchuan.csv")
df1 = data1.copy()
df1

# %%
df1=df1.drop(index=df1.index[10000:45593])
df1

# %%
df1.isna().sum()

# %%
df2= pd.concat([df, df1['PLACE_OF_SENDERS'],df1['PLACE_OF_RECEIVERS']], axis=1)
df2

# %%
df2 = df2.dropna()
df2.drop(["Buyer's city","Online retail seller"],axis=1,inplace=True)
df2

# %%
df2.isna().sum()

# %%
df2.to_csv(r"D:\Filechuan\New\Gooditem.csv", index=False)



