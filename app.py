#Import libraries
from flask import Flask, jsonify
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime as dt



#Set up the engine
engine=create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine,reflect=True)

Measurement=Base.classes.measurement
Station=Base.classes.station
session=Session(engine)

#Flask Setup
app = Flask (__name__)

#Flask Routes
@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:"
        f"Precipitation:/api/v1.0/precipitation"
        f"List of stations:/api/v1.0/stations"
        f"Observations:/api/v1.0/tobs"
        f"Dates:/api/v1.0/<start>/<end>"
    )
@app.route ("/api/v1.0/precipitation") 
def precipitation(): 
#Convert the query results to a dictionary using date as the key and prcp as the value.
    last=dt.date(2017,8,23)-dt.timedelta(days=365)
    last_d=session.query(Measurement.date).order_by(Measurment.date.desc()).first()
    precp=session.query(Measurement.date,Measurement.date).all()
    filter(Measurement.date > last).order_by(Measurement.date).all()

#Return the JSON representation of your dictionary.
    precp_data = []
    for i in precepitation:
        data={}
        data['date'] = precepitation[0]
        data['prcp'] = precipitation[1]
        precp_data.append(data)
    return jsonify(precp_data)

@app.route("/api/v1.0/stations")
def stations():
#Return a JSON list of stations from the dataset.
    session = Session(engine)
    
    stations=session.query(Station.station).all()
    
    return jsonify(stations)
@app.route("Observations:/api/v1.0/tobs")
def tobs():
    tobs_product = session.query(Measurement.station).\
    filter(Measurement.date.between('2016-08-23','2017-08-23')).all()
        observ = []
        for i in tobs_product   
        dict = {}
        dict["station"]=tobs[0]
        dict["tobs"]=float(tobs[1])
        list.append(dict)
    return jsonify(list)




#Query the dates and temperature observations of the most active station for the last year of data.


#Return a JSON list of temperature observations (TOBS) for the previous year.

@app.route ("Dates:/api/v1.0/<start>/<end>")
#Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.


#When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.


#When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.
    pass   
    
if __name__ == '__main__':
    app.run(debug=True)
