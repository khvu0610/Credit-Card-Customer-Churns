# Project Report:

## 1. Introduction

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

**Files with "-Wrangling" are Python data processing files (normalization, merging) for that specific entity.**

**Files without it are Python data visualization files for that specific entity.**

## 2. Analysis

### 2.1. Data Cleaning
In this part, I will show all the raw datasets for this project, the status and explain the plan, and how we do the concatenation and processing of the datasets.
### 2.2. Data Visualisation
#### 2.2.1. Table Inventory Information. (Warehouse)
![Figure 1 Inventory of Field & Stream Sportsman 16 Gun Fire Safe item by month of the year..png](https://github.com/khvu0610/Credit-Card-Customer-Churns/blob/fdfbee65a1788685e4925f910ff37ba6f136a880/Images/Figure%201%20Inventory%20of%20Field%20%26%20Stream%20Sportsman%2016%20Gun%20Fire%20Safe%20item%20by%20month%20of%20the%20year..png)

- **Requirement**: We are required to plot a graph showing the inventory of a specific category in all warehouses at a specific time. Because an item is only available in one stock, we choose the item with the highest sales volume.
- **Explanation**: From the requirement, we chose the File Order.csv for this figure, and all months in 2021 as the timeframe. The x-axis represents the Month, and the y-axis represents the Inventory Quantity.
- **Figure description**: As shown in the figure, the lowest amount of inventory was in February 2021 but then increased sharply in March. From April to October, the total inventory of products changed unusually but in general tended to decrease. November is the month with the highest inventory of the year.
#### 2.2.2. Overall Warehouse Inventory. (Warehouse)
![Figure 2 Inventory remainings in each warehouses over the first 3 quarters in 2022](https://github.com/khvu0610/Credit-Card-Customer-Churns/blob/72a5adc05516623fc30aff68c8330ccf570a21bf/Images/Figure%202%20Inventory%20remainings%20in%20each%20warehouses%20over%20the%20first%203%20quarters%20in%202022.png)

- **Requirement**: We are required to plot a statistical graph showing the inventory of all categories in all warehouses in a period of time. 
- **Explanation**: From the requirement, we chose the first 3 quarters in 2022 as the timeframe. This figure is plotted in a line graph, both demonstrating the trend and comparing warehouse inventory among the period to find out which warehouse is used most often. The x-axis is the time, and the y-axis is the quantity of items.
- **Figure description**: As it can be seen from the figure, the total number of items remaining in inventory dropped down gradually from the first day of 2022 to the last day of September. Only in warehouse F that the number of items in inventory was over 10000 at the end of the period whereas this number of warehouse B was nearly 8000 – the lowest. 
#### 2.2.3. Statistical chart of the presence of a specific item in purchase orders in a period. (Orders)
![Figure 3 Top 10 most purchased products..png](https://github.com/khvu0610/Credit-Card-Customer-Churns/blob/018c7704af75151448d12851fcc63234d1594900/Images/Figure%203%20Top%2010%20most%20purchased%20products..png)

- **Requirement**: We were asked to graph the presence of a particular item in purchase orders over a period.
- **Explanation**:  From the requirement, we chose the File Order.csv for this figure. To be able to easily compare the quantity of goods that customers have ordered, based on that we can see which items have the most purchases. The longer the bar, the more purchases for that item. The x-axis is the Quantity, and the y-axis is the Product Name (For each item, they have a different color).
- **Figure description**: Based on the figure, we can see that the two most ordered items by customers are Field & Stream Sportsman 16 Gun Fire Safe, and Diamondback Women's Serene Classic Comfort Bi. There is a big difference between the order quantity of these 2 products compared to the others.
#### 2.2.4. Statistical chart of the number of purchase orders of customers in a period. (Orders)
![Figure 4 Sale’s Orders on January 1, 2022.png](https://github.com/khvu0610/Credit-Card-Customer-Churns/blob/72a5adc05516623fc30aff68c8330ccf570a21bf/Images/Figure%204%20Sale%E2%80%99s%20Orders%20on%20January%201%2C%202022.png)

- **Requirement**: We were asked to do a statistical graph of the number of orders from customers over a period.
- **Explanation**: From the requirement, once again, we chose the File Order.csv for this figure. To be able to easily compare the order of goods that customers have ordered, based on that we can see which customer has the most orders. The longer the bar, the more that customer orders. The x-axis is the Number of orders, and the y-axis is the Customer Name (For each customer, they have a different color).
- **Figure description**: In general, there is not a big difference between the customers with the most purchases. Customer with Customer ID 018f915b458 has the most orders of 6, Customer ID: 8c9326adf50, fac13da56fd, 831afb47d7d, 0e2577742c5, 81dca4867d4, fe04562d0ec, 864e3735c94, 5b606bac44a has the lowest number of orders (in the top 10) is 4.

#### 2.2.5. Table’s Warehouse Selection. (Warehouse)
![Figure 5 Table’s Warehouse Selection.png](https://github.com/khvu0610/Credit-Card-Customer-Churns/blob/018c7704af75151448d12851fcc63234d1594900/Images/Figure%205%20Table%E2%80%99s%20Warehouse%20Selection.png)

- Requirement: We are required to plot a statistical graph comparing the frequency of warehouse usage for a specific good category to serve customer’s orders in a period of time. 
- Explanation: From the requirement, once again, we chose the File Gooditem.csv as the main object for this figure, and in 2021 as the timeframe. We decided to use the pie chart due to the need of comparing among different aspects. Each slice of the pie chart is the percentage of each warehouse chosen for goods delivery.
- Figure description: According to the pie chart, the warehouse is more popular than the others accounting for almost 85% of the selection. Meanwhile, the lowest selection rate belongs to warehouse B with only about 2.61%. The rest make up about 13% of the selection.

#### 2.2.6. Vehicle Usage Frequency in TN fleet. (Fleet)
![Figure 6 Vehicle Usage Frequency in TN fleet..png](https://github.com/khvu0610/Credit-Card-Customer-Churns/blob/018c7704af75151448d12851fcc63234d1594900/Images/Figure%206%20Vehicle%20Usage%20Frequency%20in%20TN%20fleet..png)

- **Requirement**: We are required to plot a statistical graph comparing the frequency of vehicle usage in a specific delivery fleet in a period of time. 
- **Explanation**: From the requirement, we chose the “TN” Fleet as the main object for this figure, and the months in 2021 as the timeframe. We can use the bar or pie chart due to the need of comparing among different aspects. And we decided to use a bar chart because there are too many aspects. The x-axis is the ID number of the vehicle, and the y-axis is the number of times that vehicle was chosen.
#### 2.2.7. Chosen Journey Frequency. (Fleet)
![Figure 7 Chosen Journey Frequency..png](https://github.com/khvu0610/Credit-Card-Customer-Churns/blob/018c7704af75151448d12851fcc63234d1594900/Images/Figure%207%20Chosen%20Journey%20Frequency..png)

- **Requirement**: We are required to plot a statistical graph comparing the frequency of chosen journey routes by a specific vehicle in a delivery fleet in a period of time. 
- **Explanation**: From the requirement, we chose the “40 FT 3XL Trailer 35MT” vehicle as the main object for this figure, the journey from senders to receivers as the main route, and months in 2021 as the timeframe. We can use the bar or pie chart due to the need of comparing among different aspects. And we decided to use a bar chart because there are too many aspects. The x-axis is the number of times that route was chosen, and the y-axis is the month in 2021.
- **Figure description**: The bar chart shows a total of 45 chosen journeys that DN fleet chose in the first 3 quarters in 2022. In general, most of them had only been used once. However, the most frequent journey was Seattle- New York with 4 times used followed by  San Francisco- New York and Seattle- Boston journey with 3 times used. Only 5 ways were used 2 times.

### 2.2.8. Difference between Sales and Cost. (Gooditem)
![Figure 8 Difference between Sales and Cost..png](https://github.com/khvu0610/Credit-Card-Customer-Churns/blob/018c7704af75151448d12851fcc63234d1594900/Images/Figure%208%20Difference%20between%20Sales%20and%20Cost..png)

- **Requirement**: We are required to plot a statistical graph showing the difference between Sales and Cost from orders. 
- **Explanation**: From the requirement, We decided to use bar plot because of the need to illustrate the sale and cost differences. The x-axis is the difference, and the y-axis is the product name. 

#### 2.2.9. Space class of each warehouse. (Warehouse)
![Figure 9 The SpaceClass of each warehouse.png](https://github.com/khvu0610/Credit-Card-Customer-Churns/blob/018c7704af75151448d12851fcc63234d1594900/Images/Figure%209%20The%20SpaceClass%20of%20each%20warehouse.png)

- **Overall description**: This chart is used to show the size of each warehouse. 
- **Explanation**: In this graph, we decided to use a bar chart. The x-axis is the type of Warehouse, and the y-axis is the size of each Warehouse. In addition, there are colors corresponding to 3 different sizes: “large”, “medium”, and “small”.
- **Figure description**: We can see that warehouse B has the largest space and warehouse F has the smallest space. The remaining warehouses have almost the same space.

#### 2.2.10. Total profit per delivery country. (Delivery)
![Figure 10 Total profit per delivery country.png](https://github.com/khvu0610/Credit-Card-Customer-Churns/blob/018c7704af75151448d12851fcc63234d1594900/Images/Figure%2010%20Total%20profit%20per%20delivery%20country.png)

- **Overall description**: This chart will show the sales profit in each different country, based on which you can see which countries consume the most. 
- **Explanation**: In this graph, we decided to use a barplot. The x-axis reflects the profit in each country, and the y-axis demonstrates the country that consumes good items.
- **Figure description**: In general, profits are highest in the two countries Francia, Alemania, decreasing in the following countries
#### 2.2.11. Top 10 cities with the most customers. (Customers)
![Figure 11 Top 10 cities with the most customers..png](https://github.com/khvu0610/Credit-Card-Customer-Churns/blob/018c7704af75151448d12851fcc63234d1594900/Images/Figure%2011%20Top%2010%20cities%20with%20the%20most%20customers..png)

- **Overall description**: This chart shows the cities with the most customers in descending order. 
- **Explanation**: In this graph, we decided to use a barplot. The x-axis reflects the city, and the y-axis demonstrates the Number of customers.
- **Figure description**: In general, a large disparity can be seen between the number of people in the city of Caguas compared to other cities. The city of Caguas has the largest number of customers, the other cities are much less and almost equal.


#### 2.2.12. Ratio of fuels used for vehicles. (Vehicle)
![Figure 12 Ratio of fuels used for vehicles..png](https://github.com/khvu0610/Credit-Card-Customer-Churns/blob/018c7704af75151448d12851fcc63234d1594900/Images/Figure%2012%20Ratio%20of%20fuels%20used%20for%20vehicles..png)

- **Overall description**: The graph shows the percentage of materials used for vehicles
- **Figure description**: According to the pie chart, Diesel fuel is more popular than other fuels, accounting for nearly 55% of choices. Meanwhile, the lowest usage rate belongs to LPG and CNG fuels with only about 0.46% and 0.66%. The rest accounted for about 44% of usage.

#### 2.2.13. Delayed products. (Gooditem)
![Figure 13 Delayed product.png](https://github.com/khvu0610/Credit-Card-Customer-Churns/blob/018c7704af75151448d12851fcc63234d1594900/Images/Figure%2013%20Delayed%20product.png)
- **Overall description**: This graph is used to summarize the delayed items and how frequent they are delayed.
- **Explanation**: In this graph we decided to use a bar chart to easily visualize our point. The bar chart will demonstrate the items name with x-axis assigned by the delay times and y-axis assigned by the product name. 
- **Figure description**: According to figure a, Diamondback Boys' Insight 24 Performance Hybr had the highest delayed times with  about 3500 times followed by Field & Stream Sportsman 16 Gun Fire Safe with around 3000 times. Meanwhile, the number of delayed Dell laptops and children’s heaters were significantly lower with no more than 500 goods being delayed. 

#### 2.2.14. Relationship between Vehicle Year of Production & Selling Price. (Vehicle Info) 

![Figure 14 Relationship between Vehicle Year of Production & Selling Price..png](https://github.com/khvu0610/Credit-Card-Customer-Churns/blob/018c7704af75151448d12851fcc63234d1594900/Images/Figure%2014%20Relationship%20between%20Vehicle%20Year%20of%20Production%20%26%20Selling%20Price..png)

- **Overall description**: This graph is used to illustrate the relationship between 2 aspects of vehicle information to see if the production year of that vehicle has any effect on the high or low price of the vehicle used for delivery. 
- **Explanation**: In this graph, we decided to use a linear regression model because both variables are quantitative. The x-axis is the production year of the vehicle, and the y-axis is the amount of money spent on the vehicle (measuring in million dollars).
- **Figure description**: We can see that the vehicle year of production only has an average positive relationship with its selling price. It means that the newer the vehicle, the higher cost it is, though the impact is not too significant with correlation coefficient at approximately 0.41. 	

#### 2.2.15. Customer’s Segment Whereabouts. (Customers)
![Figure 15 Customer’s Segment Whereabouts..png](https://github.com/khvu0610/Credit-Card-Customer-Churns/blob/018c7704af75151448d12851fcc63234d1594900/Images/Figure%2015%20Customer%E2%80%99s%20Segment%20Whereabouts..png)

- **Overall description**: This graph is used to summarize the place of living of each customer segment who are currently making orders from the company. 
- **Explanation**: In this graph, the timeframe is the first 3 quarters in 2022. We decided to use a stack bar chart to easily compare among different aspects and have an overall look. The x-axis is the region where the customers are currently living, and the y-axis is the number of customers. Each color stack of the bar represents the segment of the customers.
- **Figure description**: As it can be seen from the bar chart, the number of customers coming from the Western Europe was the highest – 5536 customers. Meanwhile, the number of Eastern Europe was only 426 people. A similar trend reflected in all 4 regions is that most of the customers are divided into the consumer segment, while the home office segment accounts for the smallest portion.

#### 2.2.16. Correlation coefficient among vehicle stats. (Vehicle)
![Figure 16 Correlation coefficient among vehicle stats..png](https://github.com/khvu0610/Credit-Card-Customer-Churns/blob/018c7704af75151448d12851fcc63234d1594900/Images/Figure%2016%20Correlation%20coefficient%20among%20vehicle%20stats..png)

- **Overall description**: This graph is used to illustrate the correlation coefficient between all aspects of vehicle information to see if the relationship between each 2 aspects is strong or weak, positive or negative.
- **Explanation**: In this graph, we decided to use a heat map to easily visualize the data. Each intersection square shows the correlation coefficient between 2 attributes: 
Closed to 1: Strong positive relationship.
Closed to -1: Strong negative relationship.
Closed to 0: Weak relationship.
- **Figure description**: We can see that most of the attributes have weak relationships with each other with the correlation coefficient getting near 0. Apart from that, engine and mileage have an average negative relationship (-0.48), meanwhile, that for the relationship between selling price and engine is average positive (0.46).

#### 2.2.17. Top 10 Best Sellers. (Delivery)

![Figure 17 Top 10 Best Sellers..png](https://github.com/khvu0610/Credit-Card-Customer-Churns/blob/018c7704af75151448d12851fcc63234d1594900/Images/Figure%2017%20Relationship%20between%20Vehicle%20Seller%20types%20and%20Selling%20price..png)

- **Overall description**: This graph is used to illustrate the relationship between 2 aspects of vehicle information to see if the type of sellers has any effect on the high or low price of the vehicle used for delivery. 
- **Explanation**: In this graph, we decided to use boxplot because there is one qualitative data and one quantitative data. The x-axis is the type of sellers, and the y-axis is the amount of money spent on the vehicle (measuring in million dollars).
- **Figure description**: We can see that dealers offered a wider range of vehicle prices, which tended to be slightly higher than those of the other 2 types of sellers. While lowest price offers often came from individuals, that from Trustmark dealers was in the middle range.

## 3. CONCLUSION

### 3.1. Achievement.
#### 3.1.1. Data.
- Overall, we have gathered data from 7 different sources of the dataset. After the data wrangling process (mainly using code) along with generating more rows and columns, our dataset has reached the required at least 10000 rows and 20 columns each.
- Our dataset has generally provided all required attributes such as Supplier, Warehouse, Customer, Item, Purchase Order, Delivery Order, Vehicle Journey, Fleet Journey, and Delivery Journey. We have also produced the missing attributes such as warehouse’s attributes with high accuracy as well as providing complete data generation principles.  

#### 3.1.2. Visualization.
- From that final dataset, 17 figures (20 graphs and charts) including 8 original requirements are drawn to help users get insight information of the dataset for the analysis of the company situation in terms of some aspects, which includes: Warehouse (Figure 1, 2, 5, 9), Orders (Figure 3, 4), Fleet (Figure 6 & 7), Gooditem (Figure 8, 13), Vehicle Information (Figure 14, 16), Customers (Figure 11 & 15), Delivery (Figure 10, 12,17).
- All charts provide a lot of useful information related to goods, journeys, vehicles, and customers making it easier for users to make decisions when working with datasets. All diagrams are drawn in the Python programming language. The charts have all the properties of a chart such as title, legend, name, number, color, etc. Some charts are even quite complex and require a lot of work from the plotters.

### 3.2. Weaknesses.
Besides the outstanding advantages mentioned, the group still has some limitations in the process of collecting and using raw data sets. The team found only 7 datasets from different sources, so the format of the datasets is not the same. The route data is not detailed yet, the group only has route data based on the city names of the sender and the receiver. Time-related attribute types are sometimes unreasonable. The rule for setting the “total_quantity_remain” column is not appropriate, resulting in the number of “Sub_categories” being negative and having to self-replicate to fill those negative values. Our team does not completely process data in code, sometimes there are columns of data that just need to be copied from another table, so doing it manually will be faster.






