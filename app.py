#Import libraries
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime as dt

from flask import Flask, jsonify

#Set up the engine
engine=create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine,reflect=True)

Measurement=Base.classes.measurement
Station=Base.classes.station
session=Session(engine)

#Flask Setup
app=Flask (_name_)

#Flask Routes
@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:"
        f"Precipitation:/api/v1.0/precipitation"
        f"List of stations:/api/v1.0/stations"
        f"Temperature:/api/v1.0/stations"
        f"Observations:/api/v1.0/tobs"
        f"Dates:/api/v1.0/<start>/<end>"
    )
@app.route ("/api/v1.0/precipitation") 
def precipitation():    
    app.run(debug=True)