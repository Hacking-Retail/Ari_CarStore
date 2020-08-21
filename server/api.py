'''API'''
import json
import sqlite3
from flask_cors import CORS
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

app.config["DEBUG"] = True

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Car Store 3000</h1>'''

#all cars route
@app.route('/api/cars/all', methods=['GET'])
def cars_all():
    conn = sqlite3.connect('cars.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_cars = cur.execute('SELECT * FROM cars;').fetchall()
    return jsonify({'cars':all_cars,
                    'status':'success'})

#filter cars route
@app.route('/api/cars', methods=['GET'])
def cars_filter():
    params = request.args
    
    #get wanted params
    car_id = params.get('id') if (params.get('id') != None ) else ''
    color_slug = params.get('color_slug')
    door_count = (params.get('door_count')) if (params.get('door_count') != None ) else ''
    engine_displacement = params.get('engine_displacement')  if (params.get('engine_displacement') != None ) else ''
    engine_power = params.get('engine_power') if (params.get('engine_power') != None ) else ''
    fuel_type = params.get('fuel_type')
    maker = params.get('maker')
    manufacture_year = params.get('manufacture_year') if (params.get('manufacture_year') != None ) else ''
    mileage = params.get('mileage') if (params.get('mileage') != None ) else ''
    model = params.get('model')
    price_eur = int(params.get('price_eur')) if (params.get('price_eur') != None ) else ''
    seat_count = params.get('seat_count') if (params.get('seat_count') != None ) else ''
    transmission = params.get('transmission')

    #params to filter
    query = "SELECT * FROM cars WHERE"
    to_filter = []

    if car_id:
        query += ' id=? AND'
        to_filter.append(car_id)

    if color_slug:
        query += ' color_slug=? AND'
        to_filter.append(color_slug)

    if door_count:
        query += ' door_count=? AND'
        to_filter.append(door_count)

    if engine_displacement:
        query += ' engine_displacement=? AND'
        to_filter.append(engine_displacement)

    if engine_power:
        query += ' engine_power=? AND'
        to_filter.append(engine_power)

    if fuel_type:
        query += ' fuel_type=? AND'
        to_filter.append(fuel_type)

    if maker:
        query += ' maker=? AND'
        to_filter.append(maker)

    if manufacture_year:
        query += ' manufacture_year=? AND'
        to_filter.append(manufacture_year)

    if mileage:
        query += ' mileage=? AND'
        to_filter.append(mileage)

    if model:
        query += ' model=? AND'
        to_filter.append(model)

    if seat_count:
        query += ' seat_count=? AND'
        to_filter.append(seat_count)

    if transmission:
        query += ' transmission=? AND'
        to_filter.append(transmission)

    if not (car_id or color_slug or door_count or engine_displacement or engine_power or fuel_type or maker 
            or manufacture_year or mileage or model or seat_count or transmission):
        return page_not_found(404)

    #remove the last "AND" and replace with ";"
    query = query[:-4] + ';'

    conn = sqlite3.connect('cars.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()

    results = cur.execute(query, to_filter).fetchall()

 
    return jsonify({'cars':results,
                    'status':'success'})


#error 404 page
@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>Page not found</p>", 404


app.run()