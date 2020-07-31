# Movie Scraper -> Dataset collection
General purpose website scraper for data analysis purposes using Scrapy.

Takes data from the Online Movie Database (OMDB) and Box Office Mojo, merging them into a single dataset.

Box Office Mojo provides box office financial data for ~800 movies. We combine this financial data with the categorical data
corresponding to each movie.

You will be asked to provide a name for your data, and this data will then be
collected and sent to the data/ folder. 

Analysis programs are forthcoming. 

Possible ML/AI
- Basic Linear Regression - Finding Trends based on variables scaled against net box office revenue 
  - compare prediction on limited data set with full data set
- k-Nearest Neighbor (kNN) /  - True-Genre Mapping (Finding Netflix Style Subgenres)
- k-Means clustering - Categorical Variable Maping
