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

PART 2: VISUALIZATION.
I. FIGURES 1 TO 8: REQUIRED TASKS
1. Table Inventory Information. (Warehouse)
Figure 1: Inventory of "Field & Stream Sportsman 16 Gun Fire Safe" item by month of the year

- Requirement: We are required to plot a graph showing the inventory of a specific category in all warehouses at a specific time. Because an item is only available in one stock, we choose the item with the highest sales volume.
- Explanation: From the requirement, we chose the File Order.csv for this figure, and all months in 2021 as the timeframe. The x-axis represents the Month, and the y-axis represents the Inventory Quantity.
- Code description: 
+) From the dataset, we create the inventory (dataframe) with the following columns: “Item Quantity in warehouse”, “Order Item Quantity”. We use the formula: df['Inventory'] = df['Item Quantity in warehouse'] - df['Order Item Quantity']. Then we create a data table df_month consisting of 2 columns, the first column is the month of the year and the second column is the inventory quantity of that item.
#Group data by month, calculate the total number of items, sort descending by quantity
df_month=df[df['order_id_date'].dt.year==2022].groupby(df['order_id_date'].dt.month)['OrderItem Quantity'].sum().reset_index().sort_values(by='Order Item Quantity', ascending=False)

+) To draw the figure we use sns.barplot then use plt.title to name the graph, use plt.xlabel to name the x-axis, use plt.ylabel to name the y-axis, plt. xticks(rotation=0)
#The inventory of a specific category in all warehouses at a specific time
sns.barplot(x='order_id_date', y='Order Item Quantity', data=df_month)
plt.title('Inventory of "Field & Stream Sportsman 16 Gun Fire Safe" item by month of the year
', fontsize=15)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Quantity', fontsize=12)
plt.xticks(rotation=0)
plt.show()

- Figure description: As shown in the figure, the lowest amount of inventory was in February 2021 but then increased sharply in March. From April to October, the total inventory of products changed unusually but in general tended to decrease. November is the month with the highest inventory of the year.
2. Overall Warehouse Inventory. (Warehouse)
Figure 2: Inventory remainings in each warehouses over the first 3 quarters in 2022

- Requirement: We are required to plot a statistical graph showing the inventory of all categories in all warehouses in a period of time. 
- Explanation: From the requirement, we chose the first 3 quarters in 2022 as the timeframe. This figure is plotted in a line graph, both demonstrating the trend and comparing warehouse inventory among the period to find out which warehouse is used most often. The x-axis is the time, and the y-axis is the quantity of items.
- Code description: 
+) For this graph, we use the Order.csv (dataframe), which has been created previously. 
+) To draw the graph, we will draw 5 lines. First, we use plt.plot() method with x assigned by “Date” (column), and y assigned by " Warehouse A - remain " (column) (both in inventory (dataframe)) to draw the first line. Then we repeat the same process for Warehouse B, C, D and F.
+) After plotting, we use plt.xlabel(), plt.ylabel(), plt.title(), plt.legend() methods to set labels, title, and legend, and plt.savefig() method to save the figure.
- Figure description: As it can be seen from the figure, the total number of items remaining in inventory dropped down gradually from the first day of 2022 to the last day of September. Only in warehouse F that the number of items in inventory was over 10000 at the end of the period whereas this number of warehouse B was nearly 8000 – the lowest. 

3. Statistical chart of the presence of a specific item in purchase orders in a period. (Orders)
Figure 3: Top 10 most purchased products.

- Requirement: We were asked to graph the presence of a particular item in purchase orders over a period.
- Explanation:  From the requirement, we chose the File Order.csv for this figure. To be able to easily compare the quantity of goods that customers have ordered, based on that we can see which items have the most purchases. The longer the bar, the more purchases for that item. The x-axis is the Quantity, and the y-axis is the Product Name (For each item, they have a different color).
- Code description: 
+) To draw the graph, we use sns.countplot() method with x assigned by “order=df['Product Name'].value_counts().iloc[:10].index” (column), y assigned by “Product Name” (column). 
+) After plotting,  use plt.title to name the graph, use plt.xlabel to name the x-axis, use plt.ylabel to name the y-axis, plt. xticks(rotation=0)

# Top 10 most purchased products
plt.figure(figsize=(12,8))
sns.countplot(y='Product Name', data=df, order=df['Product Name'].value_counts().iloc[:10].index)
plt.title('Top 10 most purchased products.', fontsize=15)
plt.xlabel('Quantity', fontsize=12)
plt.ylabel('Product Name', fontsize=12)
plt.xticks(rotation=0)
plt.show()


- Figure description: Based on the figure, we can see that the two most ordered items by customers are Field & Stream Sportsman 16 Gun Fire Safe, and Diamondback Women's Serene Classic Comfort Bi. There is a big difference between the order quantity of these 2 products compared to the others.

4. Statistical chart of the number of purchase orders of customers in a period. (Orders)
Figure 4: Sale’s Orders on January 1, 2022

- Requirement: We were asked to do a statistical graph of the number of orders from customers over a period.
- Explanation: From the requirement, once again, we chose the File Order.csv for this figure. To be able to easily compare the order of goods that customers have ordered, based on that we can see which customer has the most orders. The longer the bar, the more that customer orders. The x-axis is the Number of orders, and the y-axis is the Customer Name (For each customer, they have a different color).
- Code description: 
+) To draw the graph, we use sns.countplot() method with x assigned by “order=df['Customer Name'].value_counts().iloc[:10].index” (column), y assigned by “Product Name” (column). 
+) After plotting,  use plt.title to name the graph, use plt.xlabel to name the x-axis, use plt.ylabel to name the y-axis, plt. xticks(rotation=0)
# Top 10 customers who buy the most
plt.figure(figsize=(12,8))
sns.countplot(y='customer_id', data=df, order=df['customer_id'].value_counts().iloc[:10].index)
plt.title('Top 10 customers who buy the most', fontsize=15)
plt.xlabel('Number of orders ', fontsize=12)
plt.ylabel('Customer ID', fontsize=12)
plt.xticks(rotation=0)
plt.show()

- Figure description: In general, there is not a big difference between the customers with the most purchases. Customer with Customer ID 018f915b458 has the most orders of 6, Customer ID: 8c9326adf50, fac13da56fd, 831afb47d7d, 0e2577742c5, 81dca4867d4, fe04562d0ec, 864e3735c94, 5b606bac44a has the lowest number of orders (in the top 10) is 4.

5. Table’s Warehouse Selection. (Warehouse)
Figure 5: Table’s Warehouse Selection

- Requirement: We are required to plot a statistical graph comparing the frequency of warehouse usage for a specific good category to serve customer’s orders in a period of time. 
- Explanation: From the requirement, once again, we chose the File Gooditem.csv as the main object for this figure, and in 2021 as the timeframe. We decided to use the pie chart due to the need of comparing among different aspects. Each slice of the pie chart is the percentage of each warehouse chosen for goods delivery.
- Code description: 
+) To draw the graph, we use the syntax: df['Warehouse_block'].value_counts() to count the number of uses of each Warehouse, then use plt.pie() method with “Warehouse_block” (column) serving as the main factor slicing the pie chart and “Warehouse_block” serving as the labels.
+) After plotting, we use plt.title() method to set the title, and plt.savefig() method to save the figure.


#Tables's warehouse selection in 2021
fig, ax = plt.subplots (figsize = (10,5))
df['Warehouse_block'].value_counts().plot.pie( autopct='%1.2f%%')
plt.title("Tables's warehouse selection in 2021", fontdict = {"weight":"bold"})
plt.savefig ("Figure 5: Tables' Warehouse Selection png", box_inches="tight")
plt.show()

- Figure description: According to the pie chart, the warehouse is more popular than the others accounting for almost 85% of the selection. Meanwhile, the lowest selection rate belongs to warehouse B with only about 2.61%. The rest make up about 13% of the selection.

6. Vehicle Usage Frequency in TN fleet. (Fleet)
Figure 6: Vehicle Usage Frequency in TN fleet.

- Requirement: We are required to plot a statistical graph comparing the frequency of vehicle usage in a specific delivery fleet in a period of time. 
- Explanation: From the requirement, we chose the “TN” Fleet as the main object for this figure, and the months in 2021 as the timeframe. We can use the bar or pie chart due to the need of comparing among different aspects. And we decided to use a bar chart because there are too many aspects. The x-axis is the ID number of the vehicle, and the y-axis is the number of times that vehicle was chosen.
- Code description: 
+) From the dataset, we create the vehicle (dataframe) with the following columns: “vehicle_no”, “fleet_id”. And then, we filter the “TN” value in “fleet_id” (column) (forming DN_vehicle (dataframe)). After that, we use df.vehicleType.value_counts() method based on “vehicle_no” (column) to count the number of times each vehicle was chosen for delivery in the TN fleet based on its ID (forming Adjusted_DN_vehicle dataframe).
+) After plotting, we use plt.xlabel(), plt.ylabel(), plt.title() methods to set labels and title, plt.text() to show the frequency number on the top of the bar.
- Figure description: According to the bar chart, Mahindra LCV 1MT had the highest usage frequency with more than 600 times while 19 FT Open 7MT - MCV and 32 FT Single-Axle 7MT - HCV was the lowest. Along with Mahindra LCV 1MT, 32 FT Multi-Axle MXL 18MT and 40 FT 3XL Trailer 35MT also had more than 300 times used. Specifically, 32 FT Multi-Axle MXL 18MT was used about 600 times and DN09P9848 had more than 400 times used.
 
7. Chosen Journey Frequency. (Fleet)
Figure 7: Chosen Journey Frequency.

- Requirement: We are required to plot a statistical graph comparing the frequency of chosen journey routes by a specific vehicle in a delivery fleet in a period of time. 
- Explanation: From the requirement, we chose the “40 FT 3XL Trailer 35MT” vehicle as the main object for this figure, the journey from senders to receivers as the main route, and months in 2021 as the timeframe. We can use the bar or pie chart due to the need of comparing among different aspects. And we decided to use a bar chart because there are too many aspects. The x-axis is the number of times that route was chosen, and the y-axis is the month in 2021.
- Code description: 
+) From the dataset, we create the route (dataframe) with the five following columns which are: “vehicle_no”, “PLACE_OF_SENDERS”, “PLACE_OF_LOADING”, “PLACE_OF_DISCHARGE”, “PLACE_OF_RECEIVERS”. Next, we add another column “Route” (showing the route from the senders to the receivers) by combining “PLACE_OF_SENDERS” (column) & "PLACE_OF_RECEIVERS" (column) separated by “-”. 
+) To draw the graph, we use plt.bar() method with x assigned by “Route” (column), y assigned by "fleet_id" (column).
+) After plotting, we use plt.xlabel(), plt.ylabel(), plt.title() methods to set labels and title.
- Figure description: The bar chart shows a total of 45 chosen journeys that DN fleet chose in the first 3 quarters in 2022. In general, most of them had only been used once. However, the most frequent journey was Seattle- New York with 4 times used followed by  San Francisco- New York and Seattle- Boston journey with 3 times used. Only 5 ways were used 2 times.

8. Difference between Sales and Cost. (Gooditem)
Figure 8: Difference between Sales and Cost.

- Requirement: We are required to plot a statistical graph showing the difference between Sales and Cost from orders. 
- Explanation: From the requirement, We decided to use bar plot because of the need to illustrate the sale and cost differences. The x-axis is the difference, and the y-axis is the product name. 
- Code description: 
- First we created the profit attribute by taking the Cost of the product - Product price
- then label the x-axis with difference and y-axis with Product name, the title of this chart is “Difference between sales and costs”.

II. FIGURES 9 TO 17: ADDITIONAL CHARTS AND GRAPHS

9. Space class of each warehouse. (Warehouse)
Figure 9: The SpaceClass of each warehouse

- Overall description: This chart is used to show the size of each warehouse. 
- Explanation: In this graph, we decided to use a bar chart. The x-axis is the type of Warehouse, and the y-axis is the size of each Warehouse. In addition, there are colors corresponding to 3 different sizes: “large”, “medium”, and “small”.
- Code description: 
+) From the dataset, we use the File Warehouse.csv (dataframe) with the following columns: “spaceclass”, “warehouse_block”. 
+) To draw the graph, we use sns.countplot() method with x value assigned by “warehouse_block” (column), and y value assigned by "spaceclass" (column) (both columns in warehouse (dataframe)). 
#The SpaceClass of each warehouse
plt.figure(figsize=(10, 6))
sns.countplot(x='Warehouse_block', hue='spaceClass', data=df)
plt.title('The SpaceClass of each warehouse')
plt.show()

+) After plotting, we use plt.title() to set title, plt.savefig() to save the figure.
- Figure description: We can see that warehouse B has the largest space and warehouse F has the smallest space. The remaining warehouses have almost the same space.

10. Total profit per delivery country. (Delivery)
Figure 10: Total profit per delivery country 

- Overall description: This chart will show the sales profit in each different country, based on which you can see which countries consume the most. 
- Explanation: In this graph, we decided to use a barplot. The x-axis reflects the profit in each country, and the y-axis demonstrates the country that consumes good items.
- Code description: 
+) From the dataset, we use the file Order.csv (dataframe) with the following columns: “Order country”, and “Order Profit Per Order”. Then we create a data table df_profit consisting of 2 columns, the first column is the “Order country” and the second column is the “Order Profit Per Order”.
Syntax: 
# Group data by country, total returns with Order Status = COMPLETE, sort descending by return
df_profit = df[df['Order Status'] == 'COMPLETE'].groupby('Order Country')['Order Profit Per Order'].sum().reset_index().sort_values(by='Order Profit Per Order', ascending=False)

+) To draw the graph, we use sns.barplot() method with x value assigned by “Order country” (column), and y value assigned by "Order Profit Per Order" (column) (both columns in order (dataframe).
+) After plotting, we use plt.title() method to set the title, and plt.savefig() method to save the figure.
#Total profit per delivery country with successfully delivered orders
sns.barplot(y='Order Country', x='Order Profit Per Order', data=df_profit)
plt.title('Total profit per delivery country with successfully delivered orders', fontsize=15)
plt.xlabel('Country', fontsize=12)
plt.ylabel('Profit', fontsize=12)
plt.xticks(rotation=0)
plt.show()

- Figure description: In general, profits are highest in the two countries Francia, Alemania, decreasing in the following countries
11.Top 10 cities with the most customers. (Customers)
Figure 11: Top 10 cities with the most customers.

- Overall description: This chart shows the cities with the most customers in descending order. 
- Explanation: In this graph, we decided to use a barplot. The x-axis reflects the city, and the y-axis demonstrates the Number of customers.
- Code description: 
+) From the dataset, we use the file Customer.csv (dataframe) with the following columns: “Customer City” and “Customer ID”. 
+) To draw the graph, we use sns.barplot() method with x value assigned by “Order country” (column), and y value assigned by "Order Profit Per Order" (column) (both columns in order (dataframe).
+) After plotting, we use plt.title() method to set the title, and plt.savefig() method to save the figure.
#Group data by city, count the number of customers by unique id and sort descending
df.groupby('Customer City')['customer_id'].nunique().sort_values(ascending=False).head(10).plot.barh(figsize=(10, 5))
plt.title('10 thành phố có nhiều khách hàng nhất')
plt.xlabel('City')
plt.ylabel('Number of customers')
plt.gca().invert_yaxis()
plt.show()

- Figure description: In general, a large disparity can be seen between the number of people in the city of Caguas compared to other cities. The city of Caguas has the largest number of customers, the other cities are much less and almost equal.


12. Ratio of fuels used for vehicles. (Vehicle)
Figure 12: Ratio of fuels used for vehicles.

- Overall description: The graph shows the percentage of materials used for vehicles
- Code description: 
+) To draw the graph, we use the syntax: df['fuel'].value_counts() to count the number of vehicles using this fuel, then use plt.pie() method with “fuel” (column) serving as the main factor slicing the pie chart and “fuel” serving as the labels.
+) After plotting, we use plt.title() method to set the title, and plt.savefig() method to save the figure.
Syntax:


#Ratio of fuels used for vehicles
fig, ax = plt.subplots (figsize = (10,5))
df['fuel'].value_counts().plot.pie( autopct='%1.2f%%')
plt.title("Ratio of fuels used for vehicles", fontdict = {"weight":"bold"})
plt.savefig ("Figure 5: Tables' Warehouse Selection png", box_inches="tight")
plt.show()

- Figure description: According to the pie chart, Diesel fuel is more popular than other fuels, accounting for nearly 55% of choices. Meanwhile, the lowest usage rate belongs to LPG and CNG fuels with only about 0.46% and 0.66%. The rest accounted for about 44% of usage.

13. Delayed products. (Gooditem)
Figure 13: Delayed product
- Overall description: This graph is used to summarize the delayed items and how frequent they are delayed.
- Explanation: In this graph we decided to use a bar chart to easily visualize our point. The bar chart will demonstrate the items name with x-axis assigned by the delay times and y-axis assigned by the product name. 
- Code description: 
+) From the dataset, we create the delivery journey (dataframe) with the following columns: “Product Name”, “Delay”. After that, we use value_counts().plot method based on each of the 2 columns to count the number of products that are repeated.
+) To draw the chart in the left axes, we use ax.bar() method with x assigned by “quantity” , and y assigned by “product name” 
- Figure description: According to figure a, Diamondback Boys' Insight 24 Performance Hybr had the highest delayed times with  about 3500 times followed by Field & Stream Sportsman 16 Gun Fire Safe with around 3000 times. Meanwhile, the number of delayed Dell laptops and children’s heaters were significantly lower with no more than 500 goods being delayed. 

14. Relationship between Vehicle Year of Production & Selling Price. (Vehicle Info) 

Figure 14: Relationship between Vehicle Year of Production & Selling Price.

- Overall description: This graph is used to illustrate the relationship between 2 aspects of vehicle information to see if the production year of that vehicle has any effect on the high or low price of the vehicle used for delivery. 
- Explanation: In this graph, we decided to use a linear regression model because both variables are quantitative. The x-axis is the production year of the vehicle, and the y-axis is the amount of money spent on the vehicle (measuring in million dollars).
- Code description: 
+) For this graph, we use the vehicle_charecteristic (dataframe), which has been created previously. Besides, we use df.corr() to find the correlation coefficient between 2 variables: “year” and “selling_price (million $)”.
+) To draw the graph, we use sns.regplot() method with x value assigned by “year” (column), and y value assigned by "selling_price (million $)" (column) (both columns in vehicle_charecteristic (dataframe)). 
+) After plotting, we use plt.text() to show the correlation coefficient calculated above on the figure, plt.title() method to set title, and plt.savefig() method to save the figure.
- Figure description: We can see that the vehicle year of production only has an average positive relationship with its selling price. It means that the newer the vehicle, the higher cost it is, though the impact is not too significant with correlation coefficient at approximately 0.41. 	

15. Customer’s Segment Whereabouts. (Customers)
Figure 15: Customer’s Segment Whereabouts.

- Overall description: This graph is used to summarize the place of living of each customer segment who are currently making orders from the company. 
- Explanation: In this graph, the timeframe is the first 3 quarters in 2022. We decided to use a stack bar chart to easily compare among different aspects and have an overall look. The x-axis is the region where the customers are currently living, and the y-axis is the number of customers. Each color stack of the bar represents the segment of the customers.
- Code description: 
+) From the dataset, we create the customer (dataframe) with the following columns: “Segment”, “Order Region”. Next, we add another column “Value” (used to count for later purpose) only containing 1 value. And then, we use pd.pivot_table() for customer (dataframe) with columns assigned by “Segment”, index assigned by “Region”, values assigned by “Value”, the aggregate function being np.sum (forming customer_place).
+) To draw the graph, we define segment_info function to get the value from customer_place. Next, we will draw 3 stacks in turn: First, to draw the first stack (Consumer), we use plt.bar() with x assigned by region (a list of regions), y assigned by consumer (a list of value create by using segment_info function using “Consumer” value). To draw the second stack (Corporate), we repeat the same process using plt.bar() with x assigned by region, y assigned by corporate but having bottom = consumer. To draw the final stack (Home Office), we repeat the same process using plt.bar() with x assigned by region, y assigned by home_office but having bottom = consumer + corporate.
+) After plotting, we use plt.xlabel(), plt.ylabel(), plt.title(), plt.legend() methods to set labels, title, and legend, plt.text() to show the number of customers on the top of the bar, and plt.savefig() method to save the figure.
- Figure description: As it can be seen from the bar chart, the number of customers coming from the Western Europe was the highest – 5536 customers. Meanwhile, the number of Eastern Europe was only 426 people. A similar trend reflected in all 4 regions is that most of the customers are divided into the consumer segment, while the home office segment accounts for the smallest portion.

16. Correlation coefficient among vehicle stats. (Vehicle)
Figure 16: Correlation coefficient among vehicle stats.

- Overall description: This graph is used to illustrate the correlation coefficient between all aspects of vehicle information to see if the relationship between each 2 aspects is strong or weak, positive or negative.
- Explanation: In this graph, we decided to use a heat map to easily visualize the data. Each intersection square shows the correlation coefficient between 2 attributes: 
Closed to 1: Strong positive relationship.
Closed to -1: Strong negative relationship.
Closed to 0: Weak relationship.
- Code description: 
+) From the dataset, we create the car_info (dataframe) with the following columns: “vehicle_no”, “mileage (kmpl)”, “engine (CC)”, “selling_price”, “km_driven”. Next, we find the correlation for this dataframe using df.corr().
+) To draw the graph, we use the sns.heatmap() method using car_info.corr(). We also set annot = True  to show the correlation on each square.
+) After plotting, we use plt.title() to set title, plt.savefig() to save the figure.
- Figure description: We can see that most of the attributes have weak relationships with each other with the correlation coefficient getting near 0. Apart from that, engine and mileage have an average negative relationship (-0.48), meanwhile, that for the relationship between selling price and engine is average positive (0.46).


17. Top 10 Best Sellers. (Delivery)

Figure 17: Top 10 Best Sellers.

- Overall description: This graph is used to illustrate the relationship between 2 aspects of vehicle information to see if the type of sellers has any effect on the high or low price of the vehicle used for delivery. 
- Explanation: In this graph, we decided to use boxplot because there is one qualitative data and one quantitative data. The x-axis is the type of sellers, and the y-axis is the amount of money spent on the vehicle (measuring in million dollars).
- Code description: 
+) From the dataset, we create the vehicle_charecteristic (dataframe) with the following columns: “seats”, “owner”, “seller_type”, “fuel”, “km_driven”, “selling_price”, “year”. Next, we add another column “selling_price (million $)” (showing the selling price in million dollars) by dividing “selling_price” (column) by 1,000,000. 
+) To draw the graph, we use sns.boxplot() method with x value assigned by “seller_type” (column), and y value assigned by "selling_price (million $)" (column) (both columns in vehicle_charecteristic (dataframe)). We also set showfliers = False to remove outliers.
+) After plotting, we use plt.title() to set title, plt.savefig() to save the figure.
- Figure description: We can see that dealers offered a wider range of vehicle prices, which tended to be slightly higher than those of the other 2 types of sellers. While lowest price offers often came from individuals, that from Trustmark dealers was in the middle range.  



