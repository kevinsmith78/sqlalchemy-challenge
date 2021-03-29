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
Base=automap.base()
Base.prepare(engine,reflect=True)

Measurement=Base.classes.measurement
Station=Base.classes.station

#Flask Setup
app=Flask (_name_)

#Flask Routes
@app.route("/")
"