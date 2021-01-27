#!/usr/bin/python3
"""app variable"""

from flask import Flask, make_response, render_template
from models import storage
from api.v1.views import app_views
from flask import Blueprint, jsonify
from os import getenv

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown(e):
    storage.close()

if __name__ == "__main__":
    app.run(host=getenv('HBNB_API_HOST', default='0.0.0.0'),
            port=getenv('HBNB_API_PORT', default=5000), threaded=True)
