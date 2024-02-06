# sqlAlchemy Challenge with Climate Data
Challenge 10 for UC Berkeley Data Analytics Bootcamp. In this challenge, we use sqlAlchemy to analyze the climate data in Hawaii to plan our long holiday vacation!

### Part 1: Analyze and Explore the Climate Data
Python and SQLAlchemy are used to do a basic climate analysis and data exploration of the Hawaii climate database (found in the "Resources" folder). Specifically, SQLAlchemy ORM queries, Pandas, and Matplotlib are used to complete the analysis. Our analysis includes:  
- **Precipitation Analysis:** analyzing the precipitation (inches) in a 12-month period. The pandas library was used to plot and create a summary statistics table of the data.  
- **Station Analysis & Temperature Observations:** Designed a query to get the previous 12 months of temperature observation (TOBS) data of the most active station. Results were plotted in a histogram.

This initial analysis is saved in the jupyter notebook named "climate_data.ipynb".

### Part 2: Design Your Climate App
After completion of the initial analysis, a Flask API was designed based on the queries developed in "climate_data.ipnyb". Flask was used to create a homepage and the following API routes:
- /api/v1.0/precipitation
- /api/v1.0/stations
- /api/v1.0/tobs
- /api/v1.0/2016-08-23
- /api/v1.0/2016-08-23/2017-08-23
  
The climate app is saved in a python file named "app.py".
