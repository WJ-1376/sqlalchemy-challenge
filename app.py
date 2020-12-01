import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify



# Database Setup

engine = create_engine("sqlite:///hawaii.sqlite")

Base = automap_base()

Base.prepare(engine, reflect=True)

measurement = Base.classes.measurement




app = Flask(__name__)


##List all routes that are available.##
@app.route("/")
def HomePage():
    """List all available api routes."""
    return "Available Routes:<br/>/api/v1.0/names<br/>/api/v1.0/stations"
    
    

##/api/v1.0/precipitation##
##Convert the query results to a dictionary using date as the key and prcp as the value.##
@app.route("/api/v1.0/precipitation")
def names():
  
    session = Session(engine)

    results =  session.query(measurement.date, measurement.prcp).order_by(measurement.date).all()

    session.close()

    precipitation = []
    for precipitation, date, prcp in results:
        prec_dict = {}
        prec_dict["date"] = date
        prec_dict["prcp"] = prcp
        precipitation.append(prec_dict)

    return jsonify(precipitation)

    


@app.route("/api/v1.0/stations")
def station():
   
    session = Session(engine)

    """Return a list of station data"""
   
    results = session.query(station.station, station.name).all()

    session.close()

    
    all_station = []
    for station, name in results:
        station_dict = {}
        station_dict["station"] = station
        station_dict["name"] = name
        all_station.append(station_dict)

    return jsonify(all_station)

"""Tobs: Query the dates and temperature observations of the most active station for the last year of data."""
    @app.route("/api/v1.0/tobs")
    def tobs():
 
    results = session.query(Measurement).filter(Measurement.date.in_(str_dates))

    temp_data = []
    for day in results:
        temp_dict = {}
        temp_dict[day.date] = day.tobs
        temp_data.append(temp_dict)

    return jsonify(temp_data)

    """"/api/v1.0/<start> and /api/v1.0/<start>/<end>"""
    """Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range."""





if __name__ == '__main__':
    app.run(debug=True)
