import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import pandas as pd
import datetime as dt
from dateutil.relativedelta import relativedelta
from flask import Flask, jsonify

# Database Setup
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station
session = Session(engine)

# Calculating end date for future
a1 = session.query(func.max(Measurement.date)).all()
a2 = dt.datetime.strptime(a1[0][0], '%Y-%m-%d')
end_date = a2.strftime("%Y-%m-%d") # Latest date

# Flask Setup
app = Flask(__name__)

# Flask Routes
@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/'(start date)'/'(end date)'"
    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    result = session.query(Measurement.date, func.max(Measurement.prcp).label("precipitation"))\
            .filter(Measurement.date >= '2016-08-23').group_by(Measurement.date).all()
    res_db = pd.DataFrame(result) # Converting result into dataframe
    res_db = res_db.set_index('date') # Setting index
    res = res_db.to_dict('record') # Turns the dataframe into a dictionary
    return jsonify(res)


@app.route("/api/v1.0/stations")
def stations():
    result_stat = session.query(Station.station,Station.name).distinct().all()
    res_db = pd.DataFrame(result_stat) # Converting result into dataframe
    res_db = res_db.set_index('name') # Setting index
    r = res_db.to_dict('record') # Turns the dataframe into a dictionary
    return jsonify(r)

@app.route("/api/v1.0/tobs")
def tobs():
    result_set = session.query(func.max(Measurement.date)).all()
    tmp1 = dt.datetime.strptime(result_set[0][0], '%Y-%m-%d')
    tmp2 = tmp1 - relativedelta(years=1)
    tmp3 = tmp2.strftime("%Y-%m-%d") # One year earlier than final date, to remove hard-coded part

    result_set = session.query(Measurement.date,func.max(Measurement.tobs).label('tobs'))\
        .filter(Measurement.date >= tmp3).group_by(Measurement.date).all()
    res_db = pd.DataFrame(result_set) # Converting result into dataframe
    res_db = res_db.set_index('date') # Setting index
    res = res_db.to_dict('record') # Turns the dataframe into a dictionary

    return jsonify(res)

@app.route("/api/v1.0/temps/<start>")
@app.route("/api/v1.0/temps/<start>/<end>") #test with /api/v1.0/temps/2016-06-11/2016-06-18
def temps(start,end = end_date):
    result_set = session.query(func.min(Measurement.tobs).label('min'),
            func.max(Measurement.tobs).label('max'),
            func.avg(Measurement.tobs).label('avg'))\
        .filter(Measurement.date >= str(start), Measurement.date <= str(end)).all()
    res_db = pd.DataFrame(result_set) # Converting result into dataframe
    res = res_db.to_dict('record') # Turns the dataframe into a dictionary
    return jsonify(res) 

if __name__ == '__main__':
    app.run(debug=True)
