## Capstone

### Buiness Goal:  

Create a service to predict the revenue for the following month at any point in time. 
Create a service to predict the revenue for a specific country. 
Create a limit model to process the ten countries with the most revenue.

### Data Exploration:
1. This plot shows the trend of revenue.  
  
![plot0](https://github.com/w112358/coursera_test/blob/master/plots/0.png)

2. For the raw data, the plot below shows the relationship between different variables.
  
![plot1](https://github.com/w112358/coursera_test/blob/master/plots/1.png)

3. After feature engineering, several features, including regular previous revenues and recent views, are created from original data. The heatmap below shows the heatmap below shows the relationship between them.
  
![plot2](https://github.com/w112358/coursera_test/blob/master/plots/2.png)


### Model:
Choose the Random Forest model.

You can run the app.py file to locally start a server with flask, and then run the simulator.py file to simulate sending data and instructions with requests to the server. The prediction and re-train process can be triggered by the data and instruction. 
