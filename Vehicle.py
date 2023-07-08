# %%
import pandas as pd
import numpy as np
%matplotlib inline
import matplotlib.pyplot as plt

# %%
data = pd.read_csv("D:\Filechuan\dataset\VehicleInformation.csv")
df = data.copy()
df

# %%
data1 = pd.read_csv("D:\Filechuan\dataset\VehicleType_USA.csv")
df1 = data1.copy()
df1

# %%
df2= pd.concat([df1, df], axis=1)
df2

# %%
df2.isna().sum()

# %%
df2.drop(["torque"],axis=1,inplace=True)
df2 = df2.dropna()
df2

# %%
df2.info()

# %%
df2['max_power(bhp)']=df2['max_power(bhp)'].astype('float')

# %%
df2.to_csv(r"D:\Filechuan\New\Vehicle.csv", index=False)



