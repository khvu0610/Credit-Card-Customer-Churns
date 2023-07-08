# %%
import pandas as pd
import numpy as np

# %%
data = pd.read_csv("D:\Filechuan\dataset\DeliveryOrder.csv")
df = data.copy()
df

# %%
df.drop(['ID','Restaurant_latitude', 'Restaurant_longitude', 'Delivery_location_latitude', 'Delivery_location_longitude', 'Order_Date', 'Time_Orderd', 'Time_Order_picked','Type_of_order','Type_of_vehicle','multiple_deliveries','Festival','City'],axis=1,inplace=True)
df

# %%
data1 = pd.read_csv("D:\Filechuan\dataset\Deliverydate.csv")
df1 = data1.copy()
df1

# %%
df1.drop(['FREIGHT_FORWARDER','DELIVERED_FLAG','LAST_TRACKED_WITH_TRUCK','order_id'],axis=1,inplace=True)
df1

# %%
df1.info()

# %%
data2 = pd.read_csv("D:\Filechuan\dataset\FleetJourneyorderinfor.csv")
df2 = data2.copy()
df2

# %%
df2.drop(['Unnamed: 8'],axis=1,inplace=True)
df2

# %%
df3= pd.concat([df2['order_id'], df,df1,df2['PLACE_OF_SENDERS'],df2['PLACE_OF_RECEIVERS 1']], axis=1)
df3

# %%
df3.info()

# %%
df3=df3.drop(index=df3.index[10000:45593])

# %%
df3 = df3.reset_index(drop=True)
df3


# %%
mean1 = df3[df3['Delivery_person_Age'] != np.nan]['Delivery_person_Age'].mean()
# Thay thế giá trị np.nan bằng giá trị trung bình của cột
df3['Delivery_person_Age'] = df['Delivery_person_Age'].replace(np.nan, mean1)

mean2 = df3[df3['Delivery_person_Ratings'] != np.nan]['Delivery_person_Ratings'].mean()
# Thay thế giá trị np.nan bằng giá trị trung bình của cột
df3['Delivery_person_Ratings'] = df['Delivery_person_Ratings'].replace(np.nan, mean2)

df3['Weather'] = df3['Weather'].replace(np.nan, 'Cloudy')
df3['Road_traffic_density'] = df3['Road_traffic_density'].replace(np.nan, 'Low')
df3['Vehicle_no'] = df3['Vehicle_no'].replace(np.nan, 'KA590408')
df3['Cost_of_the_Product'] = df3['Cost_of_the_Product'].replace(np.nan, 177)
df3['Quantity'] = df3['Quantity'].replace(np.nan, 614)
df3['fuel'] = df3['fuel'].replace(np.nan, 'Diesel')
df3['name of vehicle'] = df3['name of vehicle'].replace(np.nan, 'Maruti Swift Dzire VDI')
df3['SENDERS_DATE'] = df3['SENDERS_DATE'].replace(np.nan, '18/05/2021')
df3['LOADING_DATE'] = df3['LOADING_DATE'].replace(np.nan, '27/05/2021')
df3['DISCHARGE_DATE'] = df3['DISCHARGE_DATE'].replace(np.nan, '12/06/2021')
df3['DELIVERED_DATE'] = df3['DELIVERED_DATE'].replace(np.nan, '24/06/2021')
df3['RECEIVERS_DATE'] = df3['RECEIVERS_DATE'].replace(np.nan, '28/06/2021')
df3['PREDICTED_DELIVERED_DATE'] = df3['PREDICTED_DELIVERED_DATE'].replace(np.nan, '05/07/2021')
df3

# %%
df3.info()

# %%
df3.Delivery_person_Age = df3.Delivery_person_Age.round()
df3.Delivery_person_Ratings = df3.Delivery_person_Ratings.round(2)

# %%
df3

# %%
df3.isna().sum()

# %%
df3.to_csv(r"D:\Filechuan\New\Deliveryorder.csv", index=False)



