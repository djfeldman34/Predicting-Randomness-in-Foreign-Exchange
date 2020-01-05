import os

import pandas as pd
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import Flask, jsonify, render_template
# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


#################################################
# Database Setup
#################################################

# # app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db/forex_new.db"
# # db = SQLAlchemy(app)

# # reflect an existing database into a new model
# Base = automap_base()
# # reflect the tables
# Base.prepare(db.engine, reflect=True)

# # Save references to each table
# Samples_Metadata = Base.classes.forexINFO


@app.route("/")
def home():
    """Render Home Page."""
    return render_template("index.html")

@app.route("/forex")
def forex():
    """Render Home Page."""
    return render_template("forex.html")

@app.route("/about")
def about():
    """Render Home Page."""
    return render_template("about.html")

@app.route("/fractalmachine")
def fractalmachine():
    """Render Home Page."""
    return render_template("fractalmachine.html")

@app.route("/fractals")
def fractals():
    """Render Home Page."""
    return render_template("fractals.html")

@app.route("/mandel")
def mandel():
    """Render Home Page."""
    return render_template("mandel.html")

@app.route("/mission")
def mission():
    """Render Home Page."""
    return render_template("mission.html")

@app.route("/visual1")
def visual1():
    """Render Home Page."""
    return render_template("visual1.html")

@app.route("/visual2")
def visual2():
    """Render Home Page."""
    return render_template("visual2.html")

@app.route("/visual3")
def visual3():
    """Render Home Page."""
    return render_template("visual3.html")

@app.route("/data")
def data():
    """Render Home Page."""
    return jsonify()

@app.route("/metadata/<sample>")
def sample_metadata(sample):
    """Return the MetaData for a given sample."""
    sel = [
        Samples_Metadata.sample,
        Samples_Metadata.event_date,
        Samples_Metadata.event_time,
        Samples_Metadata.loca,
        Samples_Metadata.exp_vol,
        Samples_Metadata.event_descr,
        Samples_Metadata.pred_acc,
        Samples_Metadata.unit_used,
        Samples_Metadata.act_data,
        Samples_Metadata.forc_data,
        Samples_Metadata.prev_data,
    ]

    results = db.session.query(*sel).filter(Samples_Metadata.sample == sample).all()

    sample_metadata = {}
    for result in results:
        sample_metadata["sample"] = result[0]
        sample_metadata["Event Date"] = result[1]
        sample_metadata["Event Time"] = result[2]
        sample_metadata["Location"] = result[3]
        sample_metadata["Exp Volatility"] = result[4]
        sample_metadata["Event Desc"] = result[5]
        sample_metadata["Pred Acc"] = result[6]
        sample_metadata["Unit Used"] = result[7]
        sample_metadata["Actual Data"] = result[8]
        sample_metadata["Forc Data"] = result[9]
        sample_metadata["Prev Data"] = result[10]

    print(sample_metadata)
    return jsonify(sample_metadata)

if __name__ == '__main__':
    app.run()
