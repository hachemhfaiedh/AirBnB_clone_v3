#!/usr/bin/python3
"""API status"""

from api.v1.views import app_views
from flask import Flask, jsonify
from models import storage


@app_views.route('/status', strict_slashes=False)
def status():
    return jsonify({"status": "OK"})


@app_views.route('/stats', strict_slashes=False )
def stats():
    a = {
        "Amenity": "amenities",
        "City": "cities",
        "Place": "places",
        "Review": "reviews",
        "State": "states",
        "User": "users"
        }
    b = {}
    for key, val in a.items():
        b[val] = storage.count(key)
    return jsonify(b)
