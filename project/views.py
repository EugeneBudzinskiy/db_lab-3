from flask import Blueprint
from flask import render_template
from flask import request

from classes import DataAccessor

from database import Flight
from database import Route
from database import Airport
from database import OriginAirport
from database import DestinationAirport
from database import Airline


project = Blueprint('project', __name__, template_folder="templates")


@project.route('/', methods=['GET'])
def main():
    rows_per_page = 5
    join_decode = {
        'order_by': Flight.id,
        'table_to_use': (Flight, Airline, Route, OriginAirport, DestinationAirport),
        'index_representation': {
            'flight_id': Flight.id,
            'airline_id': Airline.id,
            'origin_airport': OriginAirport.id,
            'destination_airport': DestinationAirport.id
        },
        'join_rule': (
            {'name': OriginAirport, 'on': Route.origin_airport == OriginAirport.id},
            {'name': DestinationAirport, 'on': Route.destination_airport == DestinationAirport.id},
            {'name': Flight, 'on': None},
            {'name': Airline, 'on': None}
        )
    }

    if request.method == 'GET':
        data = DataAccessor.get_all_tables(rows_per_page=rows_per_page, join_decode=join_decode,
                                           get_query_data=request.args)
        return render_template('main.html', data=data, get_query_data=request.args)


@project.route('/flight', methods=['GET', 'POST'])
def flight():
    rows_per_page = 13
    table_name = Flight
    validation_index = ['id', 'airline_id', 'flight_number', 'tail_number', 'route_id']

    if request.method == 'POST':
        DataAccessor.delete_from_table(table_name=table_name, delete_id=request.form['delete_id'])

    data = DataAccessor.get_single_table(table_name=table_name, validation_index=validation_index,
                                         get_query_data=request.args, rows_per_page=rows_per_page)

    return render_template('flight.html', data=data, get_query_data=request.args)


@project.route('/route', methods=['GET', 'POST'])
def route():
    rows_per_page = 13
    table_name = Route
    validation_index = ['id', 'origin_airport', 'destination_airport', 'time', 'distance']

    if request.method == 'POST':
        DataAccessor.delete_from_table(table_name=table_name, delete_id=request.form['delete_id'])

    data = DataAccessor.get_single_table(table_name=table_name, validation_index=validation_index,
                                         get_query_data=request.args, rows_per_page=rows_per_page)

    return render_template('route.html', data=data, get_query_data=request.args)


@project.route('/airport', methods=['GET', 'POST'])
def airport():
    rows_per_page = 13
    table_name = Airport
    validation_index = ['id', 'name']

    if request.method == 'POST':
        DataAccessor.delete_from_table(table_name=table_name, delete_id=request.form['delete_id'])

    data = DataAccessor.get_single_table(table_name=table_name, validation_index=validation_index,
                                         get_query_data=request.args, rows_per_page=rows_per_page)

    return render_template('airport.html', data=data, get_query_data=request.args)


@project.route('/airline', methods=['GET', 'POST'])
def airline():
    rows_per_page = 13
    table_name = Airline
    validation_index = ['id', 'name']

    if request.method == 'POST':
        DataAccessor.delete_from_table(table_name=table_name, delete_id=request.form['delete_id'])

    data = DataAccessor.get_single_table(table_name=table_name, validation_index=validation_index,
                                         get_query_data=request.args, rows_per_page=rows_per_page)

    return render_template('airline.html', data=data, get_query_data=request.args)
