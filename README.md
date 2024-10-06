Describe the methodology you are using, explaining the steps upi took for data cleaning, analysis, etc.
1. Projectitle:
    - ""
2. Introducing our project:
    - The corona pandemic has impacted people and businesses worldwide. At the same time, there has been a lot of information available to the public about covid.
    - Question:
     1. Have (social-)media platforms benefited and continue to benefit from the topic "Covid" ?
     2. Have health related topics gained in importance since the start of the pandemic?
    - Youtube is one of the biggest (social-)media platforms worldwide with a wide range of content.
    - With our data analysis we want to illuminate the two questions above by putting forward two Hypothesis that are to be tested:
      Since the Corona-Pandemic started:
      1. Uploads & popularity of videos about Covid have increased in the USA
      2. Uploads & popularity of videos about Health have increased in the USA
3. Our used data (and comments, main challenges, strengths & weaknesses, etc…)
    - Hopkins covid tables (csv)
    - retrieved data of Youtube API
4. Questions we want to answer  (Each question should include a conclusion written in a markdown cell.???)
    - 1. Have media platforms benefited and continue to benefit from the topic "Covid"?
    - 2. Have health related topics overall gained in importance since the beginning of the pandemic? 
5. Methodology, steps for data cleaning, analysis, ....
    1.  retrieving data (csv) from Hopkins Github Documentation
    2.  retrieving data from Youtube API
        - complications/obstacles
        -
        -
    3. 1. Data Loading and Inspection: read excel file
       2. Setting Index: The first column of the dataset, which contained the labels for various metrics like 'view_count', 'view_like_ratio', etc
       3. Sorting columns with month/Year ascending
       4. Formatting of Dates to format Month Year ('Jan 2023' e.g.)
       5. Subset Selection: For specific visualizations, we selected subsets of the data, focusing on particular metrics like view_like_ratio for selected countries (e.g., Germany, USA). This             helped narrow down the analysis to relevant data points
       6.Filtering by Date: To improve the clarity of some of the analysis, we filtered the data to include only columns (months) starting from February 2020
        7. Visualization:
            - Bar Plot: We used Seaborn to create bar plots to visualize the trends in metrics like the view-like ratio over time.
            - Linear regression with library sklearn.linear_model (LinearRegression).
              
6. Conclusions after our analysis
   1. Youtube has initially benefited from the topid "Covid" but the topic has largely lost momentum.
   2. Yes, health related topics have gained in importance since the beginning of the pandemic.

7. Links to data sources
   - [csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv](https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv)
   - https://developers.google.com/youtube/v3
   

      
