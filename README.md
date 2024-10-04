Describe the methodology you are using, explaining the steps upi took for data cleaning, analysis, etc.

1. Data Loading and Inspection: -read excel file
2. Setting Index: The first column of the dataset, which contained the labels for various metrics like 'view_count', 'view_like_ratio', etc
3. Sorting columns with month/Year
4. Formatting of Dates to format Month Year ('Jan 2023' e.g.)
5. Subset Selection: For specific visualizations, we selected subsets of the data, focusing on particular metrics like view_like_ratio for selected countries (e.g., Germany, USA). This helped narrow down the analysis to relevant data points.
6.Filtering by Date: To improve the clarity of some of the analysis, we filtered the data to include only columns (months) starting from February 2020
7. Visualization:
    Bar Plot: We used Seaborn to create bar plots to visualize the trends in metrics like the view-like ratio over time.
   Linear regression with library sklearn.linear_model (LinearRegression)
