# %%
import pandas as pd
import numpy as np
%matplotlib inline
import matplotlib.pyplot as plt

# %%
data1 = pd.read_csv("D:\Filechuan\dataset\WarehouseLease.csv")
df1 = data1.copy()
df1

# %%
df1['listingDate'] = pd.to_datetime(df1['listingDate'])

# %%
df1.info()

# %%
df1.isna().sum()

# %%
df1.drop(['Unnamed: 0','address','city','price','utilities','Region','Division'],axis=1,inplace=True)

# %%
data2 = pd.read_csv("D:\Filechuan\dataset\EcommercewarehouseinAmericanNN.csv")
df2 = data2.copy()
df2

# %%
df2.isna().sum()

# %%
df2 = df2.dropna()
print(df2)

# %%
df2.info()

# %%
df2['LOADING_DATE'] = pd.to_datetime(df2['LOADING_DATE'])
df2['DELIVERED_TO_WAREHOUSE_DATE'] = pd.to_datetime(df2['DELIVERED_TO_WAREHOUSE_DATE'])


# %%
df3= pd.concat([df1, df2], axis=1)
df3

# %%
df3.loc[df3.Warehouse_block == 'Warehouse A', 'state'] = 'Alabama'
df3.loc[df3.Warehouse_block == 'Warehouse B', 'state'] = 'California'
df3.loc[df3.Warehouse_block == 'Warehouse C', 'state'] = 'Massachusetts'
df3.loc[df3.Warehouse_block == 'Warehouse D', 'state'] = 'Newyork'
df3.loc[df3.Warehouse_block == 'Warehouse F', 'state'] = 'California'

# %%
df3.loc[df3.Warehouse_block == 'Warehouse A', 'spaceAvailable'] = 19764
df3.loc[df3.Warehouse_block == 'Warehouse B', 'spaceAvailable'] = 3600
df3.loc[df3.Warehouse_block == 'Warehouse C', 'spaceAvailable'] = 18000
df3.loc[df3.Warehouse_block == 'Warehouse D', 'spaceAvailable'] = 243072
df3.loc[df3.Warehouse_block == 'Warehouse F', 'spaceAvailable'] = 23000

# %%
df3.loc[df3.Warehouse_block == 'Warehouse A', 'spaceClass'] = 'medium'
df3.loc[df3.Warehouse_block == 'Warehouse B', 'spaceClass'] = 'small'
df3.loc[df3.Warehouse_block == 'Warehouse C', 'spaceClass'] = 'medium'
df3.loc[df3.Warehouse_block == 'Warehouse D', 'spaceClass'] = 'large'
df3.loc[df3.Warehouse_block == 'Warehouse F', 'spaceClass'] = 'medium'

# %%
df3.loc[df3.Warehouse_block == 'Warehouse A', 'listingDate'] = '2019-11-04'
df3.loc[df3.Warehouse_block == 'Warehouse B', 'listingDate'] = '2020-01-16'
df3.loc[df3.Warehouse_block == 'Warehouse C', 'listingDate'] = '2015-11-11'
df3.loc[df3.Warehouse_block == 'Warehouse D', 'listingDate'] = '2019-02-28'
df3.loc[df3.Warehouse_block == 'Warehouse F', 'listingDate'] = '2019-07-15'

# %%
df3.loc[df3.Warehouse_block == 'Warehouse A', 'spaces'] = 1
df3.loc[df3.Warehouse_block == 'Warehouse B', 'spaces'] = 1
df3.loc[df3.Warehouse_block == 'Warehouse C', 'spaces'] = 2
df3.loc[df3.Warehouse_block == 'Warehouse D', 'spaces'] = 1
df3.loc[df3.Warehouse_block == 'Warehouse F', 'spaces'] = 4

# %%
df3.loc[df3.Warehouse_block == 'Warehouse A', 'lat'] = 35.248292	
df3.loc[df3.Warehouse_block == 'Warehouse B', 'lat'] = 36.080707	
df3.loc[df3.Warehouse_block == 'Warehouse C', 'lat'] = 40.627946
df3.loc[df3.Warehouse_block == 'Warehouse D', 'lat'] = 40.771447
df3.loc[df3.Warehouse_block == 'Warehouse F', 'lat'] = 41.686778

# %%
df3.loc[df3.Warehouse_block == 'Warehouse A', 'lon'] = -80.82748		
df3.loc[df3.Warehouse_block == 'Warehouse B', 'lon'] = -80.0244
df3.loc[df3.Warehouse_block == 'Warehouse C', 'lon'] = -73.94552
df3.loc[df3.Warehouse_block == 'Warehouse D', 'lon'] = -72.94663
df3.loc[df3.Warehouse_block == 'Warehouse F', 'lon'] = -83.43943

# %%
df3.loc[df3.Warehouse_block == 'Warehouse A', 'lon'] = -80.82748		
df3.loc[df3.Warehouse_block == 'Warehouse B', 'lon'] = -80.0244
df3.loc[df3.Warehouse_block == 'Warehouse C', 'lon'] = -73.94552
df3.loc[df3.Warehouse_block == 'Warehouse D', 'lon'] = -72.94663
df3.loc[df3.Warehouse_block == 'Warehouse F', 'lon'] = -83.43943

# %%
df3.loc[df3.Warehouse_block == 'Warehouse A', 'buildingSize'] = 19764		
df3.loc[df3.Warehouse_block == 'Warehouse B', 'buildingSize'] = 3600
df3.loc[df3.Warehouse_block == 'Warehouse C', 'buildingSize'] = 18000
df3.loc[df3.Warehouse_block == 'Warehouse D', 'buildingSize'] = 243072
df3.loc[df3.Warehouse_block == 'Warehouse F', 'buildingSize'] = 23000

# %%
df3.loc[df3.Warehouse_block == 'Warehouse A', 'propType'] = 'Industrial'	
df3.loc[df3.Warehouse_block == 'Warehouse B', 'propType'] = 'Industrial'
df3.loc[df3.Warehouse_block == 'Warehouse C', 'propType'] = 'Industrial'
df3.loc[df3.Warehouse_block == 'Warehouse D', 'propType'] = 'Industrial'
df3.loc[df3.Warehouse_block == 'Warehouse F', 'propType'] = 'Industrial'

# %%
df3.loc[df3.Warehouse_block == 'Warehouse A', 'subType'] = 'Office, Retail'	
df3.loc[df3.Warehouse_block == 'Warehouse B', 'subType'] = 'Industrial'
df3.loc[df3.Warehouse_block == 'Warehouse C', 'subType'] = 'Industrial'
df3.loc[df3.Warehouse_block == 'Warehouse D', 'subType'] = 'Office, Industrial'
df3.loc[df3.Warehouse_block == 'Warehouse F', 'subType'] = 'Industrial'

# %%
df3.loc[df3.Warehouse_block == 'Warehouse A', 'yearBuilt'] = 2020
df3.loc[df3.Warehouse_block == 'Warehouse B', 'yearBuilt'] = 1995
df3.loc[df3.Warehouse_block == 'Warehouse C', 'yearBuilt'] = 1977
df3.loc[df3.Warehouse_block == 'Warehouse D', 'yearBuilt'] = 1968
df3.loc[df3.Warehouse_block == 'Warehouse F', 'yearBuilt'] = 1943

# %%
df3.loc[df3.Warehouse_block == 'Warehouse A', 'yearRenovated'] = 2021
df3.loc[df3.Warehouse_block == 'Warehouse B', 'yearRenovated'] = 2010
df3.loc[df3.Warehouse_block == 'Warehouse C', 'yearRenovated'] = 2002
df3.loc[df3.Warehouse_block == 'Warehouse D', 'yearRenovated'] = 2005
df3.loc[df3.Warehouse_block == 'Warehouse F', 'yearRenovated'] = 2002

# %%
df3.loc[df3.Warehouse_block == 'Warehouse A', 'ceilingHeight'] = 16
df3.loc[df3.Warehouse_block == 'Warehouse B', 'ceilingHeight'] = 16
df3.loc[df3.Warehouse_block == 'Warehouse C', 'ceilingHeight'] = 16
df3.loc[df3.Warehouse_block == 'Warehouse D', 'ceilingHeight'] = 16
df3.loc[df3.Warehouse_block == 'Warehouse F', 'ceilingHeight'] = 16

# %%
df3.loc[df3.Warehouse_block == 'Warehouse A', 'propInfo'] = 'new space, never previously occupied,lease rate does not include utilities, property expenses or building services'
df3.loc[df3.Warehouse_block == 'Warehouse B', 'propInfo'] = '  listed rate may not include certain utilities, building services and property expenses,can be combined with additional space(s) for up to 18,000 sf of adjacent space,listed rate may not include certain utilities, building services and property expenses,can be combined with additional space(s) for up to 18,000 sf of adjacent space a great space with high ceilings as well as private driveways.  this space has two available spots for lease, one for 8,000 square feet and the other for 10,000 square feet.  both vacancies have freight elevators as well as lift gates for the entrance.rent includes taxes and insurance. a great central location, minutes from the hutchinson river parkway and i-95.  '
df3.loc[df3.Warehouse_block == 'Warehouse C', 'propInfo'] = 'upgraded to led lighting,fenced and gated lay yard,new gas fired heaters installed 2019,front offices with reception and show/retail room  lease rate does not include utilities, property expenses or building services,2 loading docks,includes 4,800 sf of dedicated office space,central air conditioning â€¢ 19,764 sf (4,800 sf office/showroom) â€¢ 1.42 acres â€¢ 2 dock doors (8â€™x10â€™) 1 ramped to accomodate box delivery trucks â€¢ 18â€™ ceiling height â€¢ large paved fenced-in yard for outside storage and parking for 20+ vehicles â€¢ free standing building with showroom and front reception area â€¢ fully conditioned warehouse available upon request â€¢ fully sprinklered â€¢ located in industrial area with like kind buildings â€¢ power- (1) 400 amp (2) 200 amp â€¢ .85 miles from i-74 â€¢ 1.44 miles from us-70 and i-74 interchange â€¢ 3.25 miles from i-85 and i-74 interchange  fenced lot'
df3.loc[df3.Warehouse_block == 'Warehouse D', 'propInfo'] = 'available for lease,dock high & drive-in door,ceiling heights: 19 - 16,from 5,000 - 23,000 sf,hvac in warehouse,three phase power the industrial building has three phase power, hvac, and electrical drops throughout. listed rate may not include certain utilities, building services and property expenses,can be combined with additional space(s) for up to 15,000 sf of adjacent space,includes 1,500 sf of dedicated office space,1 loading dock,new space, never previously occupied,includes 1,500 sf of dedicated office space,can be combined with additional space(s) for up to 15,000 sf of adjacent space,central air conditioning,listed rate may not include certain utilities, building services and property expenses,1 drive in bay,1 loading dock,listed rate may not include certain utilities, building services and property expenses,1 loading dock,1 drive in bay,listed rate may not include certain utilities, building services and property expenses,includes 3,000 sf of dedicated office space an industrial and storage building built in 1996 & 2008 and nestled on 5.69 acres inside guilford county.  conveniently located off piedmont parkway and tarrant road with quick access to west wendover avenue and interstate 73. the property is also zoned conditional use light industrial and is serviced by a well and septic system.  storage space,air conditioning'
df3.loc[df3.Warehouse_block == 'Warehouse F', 'propInfo'] = 'convenient location just off wilkinson blvd./ easy access to the charlotte douglas airport, i-85, i-77, & all parts of charlotte $ 2250 per month listed rate may not include certain utilities, building services and property expenses excellent location. conveniently located off wilkinson blvd. with easy access to airport, i-77, & i-85.  industrial building zoned i - 2.  two pull up entrances to building and large covered patio area. rear yard is fenced. modified gross rent lease at $2250.00 per month.  24 hour access,fenced lot,signage'

# %%
df3


