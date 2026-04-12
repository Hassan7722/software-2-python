import json
from flask import Flask, Response
import mysql.connector

connection = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    database="flight_game",
    user="root",
    password="Cat"
)

app = Flask(__name__)

@app.route("/airport/<icao>")
def get_airport(icao):
    try:
        sql = "select ident as ICAO, name, municipality as Location from airport where ident = %s"
        cursor = connection.cursor(dictionary=True)
        cursor.execute(sql, (icao,))
        response = cursor.fetchone()

        if response is None:
            error_response = {
                "message": "airport not found",
            }
            return error_response, 404

        return response

    except TypeError:
        response = {
            "status": "error",
            "message": "Invalid endpoint"
        }
        return response, 404

@app.errorhandler(404)
def page_not_found(error_code):
    response = {
        "message": "Invalid endpoint",
        "status": 404
    }
    return response, 404


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3001)

