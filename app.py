# Import the dependencies.
import datetime as dt
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


# reflect an existing database into a new model

# reflect the tables


# Save references to each table


# Create our session (link) from Python to the DB


#################################################
# Flask Setup
#################################################

app = Flask(_name_)


#################################################
# Flask Routes
#################################################
@app.route('/')
def welcome():
    """List all available API routes."""
    retuen (
        f"Available Routes:<br/>"
        f"<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"- List of prior year rain totals from all stations<br/>"
        f"<br/>"
        f"/api/v1.0/stations<br/>"
        f"- List of Station numbers and names<br/>"
        f"<br/>"
        f"/api/v1.0/tobs<br/>"
        f"- List of prior year temperatures from all stations<br/>"
        f"<br/>"
        f"/api/v1.0/start<br/>"
        f"- When given the start date (YYYY-MM-DD), calculates the MIN/AVG/MAX temperature for all dates greater than and equal to the start date<br/>"
        f"<br/>"
        f"/api/v1.0/start/end<br/>"
        f"- When given the start and the end date (YYYY-MM-DD), calculate the MIN/AVG/MAX temperature for dates between the start and end date inclusive<br/>"

    )
    
  @app.route(/api/v1.0/precipitation)
    
    last_date = session.query(Measurements.date).order_by(Measurements.date.desx()).first()
    last_year = dt.date(2017,8, 23) - dt.timedelta(days=365)
    rain = sessions.query(Measurements.date, Measurements.prcp).\
                    filter (Measurements.date > last_year).\
                    order_by(Measurements.date).all()
   #create a list of dicts with 'date' and 'prcp' as teh keys and values 

    rain_totals = []
    for result in rain:
        row = {}
        row["date"] = rain[0]
        row["prcp"] = rain[1]
        rain_totals.append(row)
        
    retuen jsonify(rain_totals)

    #Retuen a JSON list of stations from dataset 
        /api/v1.0/stations
        
    def stations():
        stations_query = session.quary(Station.name, station.station)
        stations = pd.read_sql(stations_quary.statement, stations_quary.sessions.bind)
        return jsonify(stations.to_dict())
    
    
#return list of temps from prior year
@app.route(/api/v1.0/tobs)

last_date = sessions.quary(Measurements.date).order_by(Measurements.date.desc()).first()
last_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)

temperature = session.quary(Measurements.data, Measurements.tobs).\
                    filter(Measurements.date > last_year).\
                    order_by(Measurements.date).all()
#list of dicts

temperature_totals = []

for results in temperature:
    row = {}
    row["date"] = temperature[0]
    row["tobs"] = temperature[1]
    temperature_totals.append(row)
    
return jsonify(temperature_totals)



#go back one year from start date and go to end of data for min/avg/max temp

@app.route(/api/v1.0/<start>)
def trip1(start):
    
    start_date = dt.datetime.strptime(start, "%Y-%m-%d")
    last_year = dt.timedelta(days=365)
    end = dt.date(2017, 8, 23)
    trip_data = session.quary(func.min(Measurements.tobs), func.avg(Measurements.tobs), func.max(Measurements.tobs)).\
        filter(Measurements.date >= start).filter(Measurements.data <=end.all()
        trip = list(np.ravel(trip_data))
                                                  
        return jsonify(trip)
                                        
@app.route(/api/v1.0/<start>/<end>)
def trip2(start,end):

#go back one year from start/end
start_date = dt.datetime.strptime (start, "%Y-%m-%d")
end_date = dt.datetime.strptime(end, "%Y-%m-%d")
last_year = dt.timedelta(days=365)
start = start_date-last_year
end = end_date-last_year

trip_data = sessions.quary(func.min(Measurements.tobs), func.avg(Measurements.tobs), func.max(Measurements.tobs)).\
                    filter(Measurements.date >= start. filter(Measurements.date <= end).all()
                trip = list(np.ravel(trip_data))
                return jsonify(trip)

