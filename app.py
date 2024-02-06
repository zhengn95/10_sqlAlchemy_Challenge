# Import the dependencies.
from matplotlib import style
style.use('fivethirtyeight')
import matplotlib.pyplot as plt

import numpy as np
import pandas as pd
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

# Homepage with available api routes
@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/2016-08-23<br/>"
        f"/api/v1.0/2016-08-23/2017-08-23"
)

# Precipitation API route
@app.route("/api/v1.0/precipitation")
def precipitation():
    """Return a list of precipitation data in the last 12 months"""
    most_recent_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    year_ago = dt.datetime.strptime(most_recent_date[0], '%Y-%m-%d').date() - dt.timedelta(365)
    last_12_months = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= year_ago).\
        all()

    # Create a list of dictionaries with date as key and precipitation as value
    precipitation = {}
    for date, prcp in last_12_months:
        precipitation[date] = prcp
    
    return jsonify(precipitation)

# Stations API route
@app.route("/api/v1.0/stations")
def station():
    """Return a list of stations from the dataset"""
    all_stations = session.query(Station.station).all()
    list_stations = list(np.ravel(all_stations))

    return jsonify(list_stations)

# Temperature Observation API route
@app.route("/api/v1.0/tobs")
def tobs():
    """Return the dates and Tobs of the most-active station for the previous year"""
    most_active = session.query(Measurement.date, Measurement.tobs).\
        filter(Measurement.station=='USC00519281').all()
    list_most_active = list(np.ravel(most_active))
    
    return jsonify(list_most_active)

# Specified start API route
@app.route("/api/v1.0/2016-08-23")
def start():
    """Return TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date."""
    Tstart_date = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs),\
        func.max(Measurement.tobs)).\
        filter(Measurement.date >= '2016-08-23').\
        order_by(Measurement.date).all()
    Tstart_list = list(np.ravel(Tstart_date))

    return jsonify(Tstart_list)

# Specifed start/end API route
@app.route("/api/v1.0/2016-08-23/2017-08-23")
def start_end():
    """Return TMIN, TAVG, and TMAX for the dates from the start date to the end date"""
    Tstartend_date = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs),\
        func.max(Measurement.tobs)).\
        filter(Measurement.date >= '2016-08-23').\
        filter(Measurement.date <= '2017-08-23').\
        order_by(Measurement.date).all()
    Tstartend_list = list(np.ravel(Tstartend_date))

    return jsonify(Tstartend_list)


session.close()

if __name__ == '__main__':
    app.run(debug=True)











        


