'''API'''
import json
from flask import Flask, request, jsonify

app = Flask(__name__)
app.config["DEBUG"] = True

#get datas
data = json.load(open('Dataset-Hackathon.json'))

#basic route
@app.route('/', methods=['GET'])
def index():
    return """ <h1> Bienvenue sur CarStore3000 </h1> 
            <p>Commencez dès maintenant à chercher votre futur véhicule d'occasion</p>
            <a href="">Commencer la recherche</a>
            """


#all cars route
@app.route('/api/v1/resources/cars/all', methods=['GET'])
def cars_all():
    return jsonify(data)

#filter cars route
@app.route('/api/v1/resources/cars', methods=['GET'])
def cars_filter():
    params = request.args
    
    #get wanted params
    car_id = int(params.get('id')) if (params.get('id') != None ) else ''
    color_slug = params.get('color_slug')
    door_count = int(params.get('door_count')) if (params.get('door_count') != None ) else ''
    engine_displacement = int(params.get('engine_displacement'))  if (params.get('engine_displacement') != None ) else ''
    engine_power = int(params.get('engine_power')) if (params.get('engine_power') != None ) else ''
    fuel_type = params.get('fuel_type')
    maker = params.get('maker')
    manufacture_year = int(params.get('manufacture_year')) if (params.get('manufacture_year') != None ) else ''
    mileage = int(params.get('mileage')) if (params.get('mileage') != None ) else ''
    model = params.get('model')
    price_eur = int(params.get('price_eur')) if (params.get('price_eur') != None ) else ''
    seat_count = int(params.get('seat_count')) if (params.get('seat_count') != None ) else ''
    transmission = params.get('transmission')

    #params to filter
    filterParams = {}
    print(params)

    if car_id:
        filterParams.update({"id": car_id})

    if color_slug:
        filterParams.update({"color_slug": color_slug})

    if door_count:
        filterParams.update({"door_count": door_count})

    if engine_displacement:
        filterParams.update({"engine_displacement": engine_displacement})

    if engine_power:
        filterParams.update({"engine_power": engine_power})

    if fuel_type:
        filterParams.update({"fuel_type": fuel_type})

    if maker:
        filterParams.update({"maker": maker})

    if manufacture_year:
        filterParams.update({"manufacture_year": manufacture_year})

    if mileage:
        filterParams.update({"mileage": mileage})

    if model:
        filterParams.update({"model": model})

    if seat_count:
        filterParams.update({"seat_count": seat_count})

    if transmission:
        filterParams.update({"transmission": transmission})

    data_del = []
    print(filterParams)

    for key, value in filterParams.items():
        for car in data:
            if car[key]!=value:
                data_del.append(car)

    data_result = [x for x in data if x not in data_del]


    if not (car_id or color_slug or door_count or engine_displacement or engine_power or fuel_type or maker 
            or manufacture_year or mileage or model or seat_count or transmission):
        return page_not_found(404)

 
    return jsonify(data_result)


#filter id cars route
@app.route('/api/v1/resources/cars', methods=['GET'])
def cars_filter_id():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."
    results = []

    for car in data:
        if car['id'] == id:
            results.append(car)

    return jsonify(results)

#error 404 page
@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>Page not found</p>", 404


app.run()