# Assignment Background - Hawaii Climate Analysis

## SQLAlchemy Setup

To begin, use Python and SQLAlchemy to do basic climate analysis and data exploration of your climate database. All of the following analysis should be completed using SQLAlchemy ORM queries, Pandas, and Matplotlib.

Next, I used SQLAlchemy's `create_engine` to connect to your sqlite database, and `automap_base()` to reflect the tables into classes to be saved as classes called `Station` and `Measurement`.

### Exercise 1 - Precipitation Analysis

Using the database, I queried precipitation data for the past 12 months of the data set. This data was then added to a Pandas dataframe and plotted to produce the following plot and summary statistics within the precipitation data.

  ![precipitation](Images/precipitation.png)

### Exercise 2 - Station Analysis

Using the same database, I then queried station information to find out which stations are the most active and which had the highest number of observations. I took the station with the highest amount of observations, and plotted its temperature observation count as a histogram.

![station-histogram](Images/station-histogram.png)

- - -

## Step 2 - Climate Flask App

With my initial analysis finished, I built a python flask app that utlizes the above queries to allow users to explore the data.

### Available Routes:

* `/`

  * Home page containing all routes

* `/api/v1.0/precipitation`

  * JSONified dictionary containing `date` and `prcp` values.

* `/api/v1.0/stations`

  * JSON list of stations from the dataset.

* `/api/v1.0/tobs`
  
  * JSON containing the past 12 months of Temperature Observations (tobs) data.

* `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`

  * Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range. If no end date is supplied, it returns the temperatures for the given day only.

---
## Copyright

Data Boot Camp ©2019. All Rights Reserved.
