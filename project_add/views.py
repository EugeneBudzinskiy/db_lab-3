from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect

from classes import BusinessLogic
from classes import DataAccessor

from database import Flight
from database import Route
from database import Airport
from database import Airline

project_add = Blueprint('project_add', __name__, template_folder="templates")


@project_add.route('/add-flight', methods=['GET', 'POST'])
def add_flight():
    table_name = Flight
    data = None
    validation_result = None

    data_decode = {
        'id': {'unique': True, 'connected': None, 'regex': '^(([A-Z0-9]+)-)+[A-Z0-9]+$'},
        'airline_id': {'unique': True, 'connected': Airline, 'regex': '^[A-Z0-9]+$'},
        'flight_number': {'unique': False, 'connected': None, 'regex': '^[0-9]+$'},
        'tail_number': {'unique': False, 'connected': None, 'regex': '^[A-Z0-9]+$'},
        'route_id': {'unique': True, 'connected': Route, 'regex': '^[A-Z0-9]+-[A-Z0-9]+$'}
    }

    if request.method == 'POST':
        data = DataAccessor.collect_data_to_dict(collect=request.form, keys=data_decode.keys())
        validation_result = \
            BusinessLogic.validate_addition(table_name=table_name, data=data, data_decode=data_decode)

        if all(el is None for el in validation_result.values()):
            DataAccessor.create_in_table(table_name=table_name, data=data, column_to_create=data_decode.keys())
            return redirect('flight')

    return render_template('add_flight.html', data=data, validation_result=validation_result)


@project_add.route('/add-route', methods=['GET', 'POST'])
def add_route():
    table_name = Route
    data = None
    validation_result = None

    data_decode = {
        'id': {'unique': True, 'connected': None, 'regex': '^[A-Z0-9]+-[A-Z0-9]+$'},
        'origin_airport': {'unique': True, 'connected': Airport, 'regex': '^[A-Z0-9]+$'},
        'destination_airport': {'unique': True, 'connected': Airport, 'regex': '^[A-Z0-9]+$'},
        'time': {'unique': False, 'connected': None, 'regex': '^[0-9]+$'},
        'distance': {'unique': False, 'connected': Route, 'regex': '^[0-9]+$'}
    }

    if request.method == 'POST':
        data = DataAccessor.collect_data_to_dict(collect=request.form, keys=data_decode.keys())
        validation_result = \
            BusinessLogic.validate_addition(table_name=table_name, data=data, data_decode=data_decode)

        if all(el is None for el in validation_result.values()):
            DataAccessor.create_in_table(table_name=table_name, data=data, column_to_create=data_decode.keys())
            return redirect('route')

    return render_template('add_route.html', data=data, validation_result=validation_result)


@project_add.route('/add-airport', methods=['GET', 'POST'])
def add_airport():
    table_name = Airport
    data = None
    validation_result = None

    data_decode = {
        'id': {'unique': True, 'connected': None, 'regex': '^[A-Z0-9]+$'},
        'name': {'unique': False, 'connected': None, 'regex': '^.+$'}
    }

    if request.method == 'POST':
        data = DataAccessor.collect_data_to_dict(collect=request.form, keys=data_decode.keys())
        validation_result = \
            BusinessLogic.validate_addition(table_name=table_name, data=data, data_decode=data_decode)

        if all(el is None for el in validation_result.values()):
            DataAccessor.create_in_table(table_name=table_name, data=data, column_to_create=data_decode.keys())
            return redirect('airport')

    return render_template('add_airport.html', data=data, validation_result=validation_result)


@project_add.route('/add-airline', methods=['GET', 'POST'])
def add_airline():
    table_name = Airline
    data = None
    validation_result = None

    data_decode = {
        'id': {'unique': True, 'connected': None, 'regex': '^[A-Z0-9]+$'},
        'name': {'unique': False, 'connected': None, 'regex': '^.+$'}
    }

    if request.method == 'POST':
        data = DataAccessor.collect_data_to_dict(collect=request.form, keys=data_decode.keys())
        validation_result = \
            BusinessLogic.validate_addition(table_name=table_name, data=data, data_decode=data_decode)

        if all(el is None for el in validation_result.values()):
            DataAccessor.create_in_table(table_name=table_name, data=data, column_to_create=data_decode.keys())
            return redirect('airline')

    return render_template('add_airline.html', data=data, validation_result=validation_result)
