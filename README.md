# Price Hills, Sales Climbs
## Grocery Items Price vs Sales

**Luke Hobbs**: 

### Business problem:
1. What correlates to increased item store sales?
- It sounds intuitive: the higher the price, the lower the demand. Customers want to economise, catch golden deals, and feel respected. 
Nonetheless, a coursery look at Item Store Sales data paints a more nuanced portrait. 
2. Our stakeholders are the grocery outlet owners
3. The aim is to increase sales revenue
4. The plan is to adapt and modify businesses based on actionable, analytics backed information

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
### A default linear regression model: ![](Prediction-of-Product-Sales_Project1_Part6_core ipynb at main · Rovidicus_Prediction-of-Product-Sales](https://github.com/Rovidicus/Prediction-of-Product-Sales/assets/141533406/854b5aff-b40f-4364-8e4d-1dff5ed52cbc)

### Here are examples of how to embed images from your sub-folder


#### Visual 1 Title
![sample image](project1_sample_image.png)

> Sentence about visualization.

#### Visual 2 Title

## Model

Describe your final model

Report the most important metrics

Refer to the metrics to describe how well the model would solve the business problem

## Recommendations:

More of your own text here


## Limitations & Next Steps

More of your own text here



# Prediction-of-Product-Sales
## Sales prediction model for food items sold at various stores
1. Using a histogram, I got a bird's eye view of product weights as well as how many weights remain unaccounted for with the bar left of 0.

![WeightDistribution](https://github.com/Rovidicus/Prediction-of-Product-Sales/assets/141533406/90fa1148-399b-4ac8-b97e-b7f62793359c)

2. Another histogram displays the maximum retail price of items

![MaxRetailPrice](https://github.com/Rovidicus/Prediction-of-Product-Sales/assets/141533406/570d2014-0b75-4a92-b813-d4e744746965)

3. This group boxplot gives an idea of sales figures by store size. It may be curious why medium sized stores outperform the other stores, but some data is still missing.

![SalesbySizeBoxplots](https://github.com/Rovidicus/Prediction-of-Product-Sales/assets/141533406/6e68cdb9-b4fa-4256-a50c-44f4459abe43)

4. Here is a violin plot of item store sales by store type. The type 3 supermarket well outperforms its siblings with grocery stores only yeilding a fraction of sales.

![SalesbyStoreViolin](https://github.com/Rovidicus/Prediction-of-Product-Sales/assets/141533406/7a6d847a-caa5-42e4-8896-af53f935e999)

5. I made a countplot of item types sorted by fat content. Only in meat and breakfast did "Regular" display more than "Low Fat".

![ItemTypeFatContent](https://github.com/Rovidicus/Prediction-of-Product-Sales/assets/141533406/844100e9-c7cc-4c22-b057-3e904c4d04ed)

6. A masked heatmap of the numerical data shows a moderate correlation of 0.57 between Item Store Sales and Max Retail Price

![Heatmap](https://github.com/Rovidicus/Prediction-of-Product-Sales/assets/141533406/ac43df22-4407-43b5-9c0b-da13e8405c16)
