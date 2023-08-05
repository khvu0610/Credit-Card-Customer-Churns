# Personal Project:
**Purpose**: Building a dataset for transportation (delivery) orders to facilitate information exploitation and find optimal delivery routes from suppliers to transit warehouses, and from transit warehouses to customers. The project aims to arrange delivery orders to reach customers within the desired timeframe, optimize inventory retrieval from warehouses, maximize the fleet's capacity, select the least costly routes for vehicles, transport the maximum amount of goods on each leg, etc.

**Information**: 10,000 records/objects (each object contains at least 20 attributes). The dataset includes the following entities: Supplier (Warehouse), Transit Warehouse (Warehouse), Customer (Customer), Goods (Gooditem), Purchase Order (Order), Delivery Order (DeliveryOrder), Vehicle (Vehicle), Fleet Journey (FleetJourney), Vehicle Journey (VehicelJourney), and Delivery Journey (DeliveryJourney) (showing which warehouse/supplier, customers, and returning to which warehouse).

**Step 1**: Search for existing datasets: Find 10 different datasets on Kaggle.

**Step 2**: Supplement, modify, normalize, and merge into a complete dataset as required: Based on the 10 found datasets, normalize and merge them into the specified file format (under **Information**).

**Step 3**: Analyze the data and visualize as requested:
For each type of entity, create one analytical chart and one custom statistical chart matching the project's objectives.
Additionally, create the following charts to serve specific purposes:
- Chart showing the inventory level of a specific item in all warehouses at a given time.
- Statistical chart of the quantity (or value) of goods imported/exported in all warehouses during a period.
- Statistical chart of the presence of a specific item in purchase orders during a period.
- Statistical chart of the number of purchase orders from customers during a period.
- Chart comparing the frequency of selecting warehouses to retrieve an item during a period.
- Chart comparing the frequency of using vehicles within the fleet during a period.
- Chart comparing the frequency of using routes by vehicles in the fleet during a period.
- Chart showing the revenue difference from delivery orders / transportation costs during a period.

**Files with -Wrangling are Python data processing files (normalization, merging) for that specific entity.**
**Files without it are Python data visualization files for that specific entity.**

In addition, I also made a detailed report about this project, to have the insights I found about the project, please click on the link below:

**Final Report**: https://docs.google.com/document/d/1yqVyse-NGpIDU8vGTWmRku0iqsa8eXDxZUQ6HB5BH5s/edit?usp=sharing 

**Slide Report**: https://www.canva.com/vi_vn/mau/?category=tAExRLg81RI&fFormat=0BR
