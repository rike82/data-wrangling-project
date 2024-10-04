Describe the methodology you are using, explaining the steps upi took for data cleaning, analysis, etc.
1. Projectitle:
    - ""
2. Introducing our project:
    - "" (aus Präsi)
3. Our used data (and comments, main challenges, strengths & weaknesses, etc…)
    - Hopkins covid tables (csv)
    - retrieved data of Youtube API
4. Questions we want to answer  (Each question should include a conclusion written in a markdown cell.???)
    - 1. Have media platforms benefited and continue to benefit from the topic "Covid"?
    - 2. Have health related topics overall gained in importance since the beginning of the pandemic? 
5. Methodology, steps for data cleaning, analysis, ....
    1. retrieving data (csv) from Hopkins .....
    2. retrieving data from Youtube API
        -
        -
        -
    3. 1. Data Loading and Inspection: -read excel file
       2. Setting Index: The first column of the dataset, which contained the labels for various metrics like 'view_count', 'view_like_ratio', etc
       3. Sorting columns with month/Year ascending
       4. Formatting of Dates to format Month Year ('Jan 2023' e.g.)
       5. Subset Selection: For specific visualizations, we selected subsets of the data, focusing on particular metrics like view_like_ratio for selected countries (e.g., Germany, USA). This             helped narrow down the analysis to relevant data points
       6.Filtering by Date: To improve the clarity of some of the analysis, we filtered the data to include only columns (months) starting from February 2020
              
6. Conclusions after our analysis
   -
7. Further questions (???)
   -
8. Links to data sources and Trello
       -

7. Visualization:
    Bar Plot: We used Seaborn to create bar plots to visualize the trends in metrics like the view-like ratio over time.
   Linear regression with library sklearn.linear_model (LinearRegression)

8. Coclusions:
      
