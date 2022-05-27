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

project_edit = Blueprint('project_edit', __name__, template_folder="templates")


@project_edit.route('/edit-flight', methods=['GET', 'POST'])
def edit_flight():
    table_name = Flight
    validation_result = None
    column_to_edit = ['id', 'airline_id', 'flight_number', 'tail_number', 'route_id']

    data_decode = {
        'id': {'unique': False, 'connected': None, 'regex': '^(([A-Z0-9]+)-)+[A-Z0-9]+$'},
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
            DataAccessor.update_in_table(table_name=table_name, edit_id=request.form['edit_id'], data=data,
                                         column_to_edit=column_to_edit)
            return redirect('flight')

        else:
            return render_template('edit_flight.html', data=data, validation_result=validation_result)

    elif request.method == 'GET':
        data = DataAccessor.read_from_table(table_name=table_name, read_id=request.args['id'])
        return render_template('edit_flight.html', data=data, validation_result=validation_result)


@project_edit.route('/edit-route', methods=['GET', 'POST'])
def edit_route():
    table_name = Route
    validation_result = None
    column_to_edit = ['id', 'origin_airport', 'destination_airport', 'time', 'distance']

    data_decode = {
        'id': {'unique': False, 'connected': None, 'regex': '^[A-Z0-9]+-[A-Z0-9]+$'},
        'origin_airport_id': {'unique': True, 'connected': Airport, 'regex': '^[A-Z0-9]+$'},
        'destination_airport_id': {'unique': True, 'connected': Airport, 'regex': '^[A-Z0-9]+$'},
        'time': {'unique': False, 'connected': None, 'regex': '^[0-9]+$'},
        'distance': {'unique': False, 'connected': Route, 'regex': '^[0-9]+$'}
    }

    if request.method == 'POST':
        data = DataAccessor.collect_data_to_dict(collect=request.form, keys=data_decode.keys())
        validation_result = \
            BusinessLogic.validate_addition(table_name=table_name, data=data, data_decode=data_decode)

        if all(el is None for el in validation_result.values()):
            DataAccessor.update_in_table(table_name=table_name, edit_id=request.form['edit_id'], data=data,
                                         column_to_edit=column_to_edit)
            return redirect('route')

        else:
            return render_template('edit_route.html', data=data, validation_result=validation_result)

    elif request.method == 'GET':
        data = DataAccessor.read_from_table(table_name=table_name, read_id=request.args['id'])
        return render_template('edit_route.html', data=data, validation_result=validation_result)


@project_edit.route('/edit-airport', methods=['GET', 'POST'])
def edit_airport():
    table_name = Airport
    validation_result = None
    column_to_edit = ['id', 'name']

    data_decode = {
        'id': {'unique': False, 'connected': None, 'regex': '^[A-Z0-9]+$'},
        'name': {'unique': False, 'connected': None, 'regex': '^.+$'}
    }

    if request.method == 'POST':
        data = DataAccessor.collect_data_to_dict(collect=request.form, keys=data_decode.keys())
        validation_result = \
            BusinessLogic.validate_addition(table_name=table_name, data=data, data_decode=data_decode)

        if all(el is None for el in validation_result.values()):
            DataAccessor.update_in_table(table_name=table_name, edit_id=request.form['edit_id'], data=data,
                                         column_to_edit=column_to_edit)
            return redirect('airport')

        else:
            return render_template('edit_airport.html', data=data, validation_result=validation_result)

    elif request.method == 'GET':
        data = DataAccessor.read_from_table(table_name=table_name, read_id=request.args['id'])
        return render_template('edit_airport.html', data=data, validation_result=validation_result)


@project_edit.route('/edit-airline', methods=['GET', 'POST'])
def edit_airline():
    table_name = Airline
    validation_result = None
    column_to_edit = ['id', 'name']

    data_decode = {
        'id': {'unique': False, 'connected': None, 'regex': '^[A-Z0-9]+$'},
        'name': {'unique': False, 'connected': None, 'regex': '^.+$'}
    }

    if request.method == 'POST':
        data = DataAccessor.collect_data_to_dict(collect=request.form, keys=data_decode.keys())
        validation_result = \
            BusinessLogic.validate_addition(table_name=table_name, data=data, data_decode=data_decode)

        if all(el is None for el in validation_result.values()):
            DataAccessor.update_in_table(table_name=table_name, edit_id=request.form['edit_id'], data=data,
                                         column_to_edit=column_to_edit)
            return redirect('airline')

        else:
            return render_template('edit_airline.html', data=data, validation_result=validation_result)

    elif request.method == 'GET':
        data = DataAccessor.read_from_table(table_name=table_name, read_id=request.args['id'])
        return render_template('edit_airline.html', data=data, validation_result=validation_result)
