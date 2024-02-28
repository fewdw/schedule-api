from app import app
from flask import request, jsonify

@app.errorhandler(404)
def not_found_error(error):
    return jsonify({"error" : str(error)}), 404


@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({"error" : str(error)}), 500
