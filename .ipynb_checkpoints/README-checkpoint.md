# Grocery Sales Investigation

**Luke Hobbs**: 

### Business problem: How can we improve item sales?
1. What correlates to increased item store sales?
2. Stakeholders: grocery outlet owners
3. Aim: increase sales revenue
4. Plan: adapt and modify businesses based on actionable, analytics backed information

### Data:
Data can include source and high-level description (e.g. # obs)
#### Here is the provided spreadsheet of item and outlet information: [Grocery Item Sales](https://drive.google.com/file/d/1syH81TVrbBsdymLT_jl2JIf6IjPXtSQw/view)
#### The dataset houses information on both the items and outlets in which they were sold, factoring in nine feature columns (Item ID excluded) to explore correlations with item sales.

## Methods
- This dataset has 8523 rows, and 12 columns. As mentioned above, Item ID column was dropped as it's a high cardinality feature not useful for analysis, leaving 10 features with the target, Item_Outlet_Sales.
- No duplicates detected but some null values. A quick visual of missing values:
  ![](https://github.com/Rovidicus/Prediction-of-Product-Sales/assets/141533406/c675b525-7e35-4d41-913a-a7a038badbf6)
### Categorical columns displayed: ['Item_Fat_Content', 'Item_Type', 'Outlet_Identifier', 'Outlet_Location_Type', 'Outlet_Type']
-   A for loop of object column value counts revealed Item Fat Content had entry errors which were sorted to just Low Fat and Regular.
-   Columns were one hot encoded with simple imputation
### Only one ordinal column: Outlet Size
-   Outlet Size had an awkward label of "High" which I changed to "Large"
-   So many values were missing they were imputed into their own constant. Feature was encoded smallest to largest, missing last.
### Numeric columns displayed: ['Item_Weight', 'Item_Visibility', 'Item_MRP', 'Outlet_Establishment_Year', 'Item_Outlet_Sales']
-   Statistics of columns was checked for strange and impossible values. Item Visibility had 526 values at 0%. Obviously every item has some percentage visibility.
-     Mean was imputed for missing values with standard scaling.
## Results

### Standard linear regression model: 
------------------------------------------------------------
Regression Metrics: Training Data
------------------------------------------------------------
- MAE = 847.126
- MSE = 1,297,559.357
- RMSE = 1,139.105
- R^2 = 0.562

------------------------------------------------------------
Regression Metrics: Test Data
------------------------------------------------------------
- MAE = 804.105
- MSE = 1,194,333.006
- RMSE = 1,092.855
- R^2 = 0.567

### Random Forest

------------------------------------------------------------
Regression Metrics: Training Data
------------------------------------------------------------
- MAE = 661.548
- MSE = 889,858.636
- RMSE = 943.323
- R^2 = 0.699

------------------------------------------------------------
Regression Metrics: Test Data
------------------------------------------------------------
- MAE = 733.109
- MSE = 1,113,840.201
- RMSE = 1,055.386
- R^2 = 0.596

## Model

The Linear Regression model had high bias with training and testing data similarly low in r2 and other metrics.
The Random Forest model scored much higher on training r2 and a little higher on testing r2. It's not ready for deployment but may be on the right track with some parameter tweaking.
As is, the Random Forest can only account for about 60% error. A bagged tree model may be useful to deploy in future.

1. A masked heatmap of the numerical data shows a moderate correlation of 0.57 between Item Store Sales and Max Retail Price

![Heatmap](https://github.com/Rovidicus/Prediction-of-Product-Sales/assets/141533406/ac43df22-4407-43b5-9c0b-da13e8405c16)

2. Here is a comparison of Max Retail Price to Item Sales, a direct positive correlation visualized.

![Price Sales](https://github.com/Rovidicus/Prediction-of-Product-Sales/assets/141533406/c06ed4c2-bc5d-4186-85d8-6782b7120132)

3. Strangely there is an inverse correlation of percentage visibility in a store with that item's sales.

![Visibility Sales](https://github.com/Rovidicus/Prediction-of-Product-Sales/assets/141533406/6b86fd04-dcfd-43a9-8bd6-48ab28b5c00a)

## Coefficient Results

1. This is a bar plot of coefficients using linear regression. Seafood and starchy food show strong sales returns with dairy and 'other' items returning poor figures.

![LinRegCoeff](https://github.com/Rovidicus/Prediction-of-Product-Sales/assets/141533406/c67c6c54-5982-4336-8ec0-5c434a2d97d4)

2. Here we have a plot with a random forest that returned better metrics in modeling than the linear regressor. Max Retail Price appears again to be an indicator of great sales.

![RandomForestCoeff](https://github.com/Rovidicus/Prediction-of-Product-Sales/assets/141533406/ca4ca146-63b2-4079-b47b-ec2797deef44)

### Some food items are staples in diets for which there'll be a constant and convenient demand for (like starchy foods and seafood). Given the positive correlation with higher prices and higher sales, such foods in consistent demand would be more inelastic to price markup. 
### Other items is more difficult to say as they may be more niche and have limited demand that would be stifled by higher prices.

## By Store



For any additional questions, please contact me at rovidicus@hotmail.com
