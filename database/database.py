from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class Airport(db.Model):
    __tablename__ = 'airport'

    id = db.Column(db.String(10), primary_key=True)
    name = db.Column(db.String(256), nullable=False)

    def __init__(self, **kwargs):
        self.id = kwargs['id']
        self.name = kwargs['name']

    def __repr__(self):
        return f"ID: {self.id} - Name: {self.name}"


class Route(db.Model):
    __tablename__ = 'route'

    id = db.Column(db.String(10), primary_key=True)
    origin_airport = db.Column(db.String(10), db.ForeignKey('airport.id', ondelete="CASCADE"), nullable=False)
    destination_airport = db.Column(db.String(10), db.ForeignKey('airport.id', ondelete="CASCADE"), nullable=False)
    time = db.Column(db.Integer, nullable=False)
    distance = db.Column(db.Integer, nullable=False)

    def __init__(self, **kwargs):
        self.id = kwargs['id']
        self.origin_airport = kwargs['origin_airport']
        self.destination_airport = kwargs['destination_airport']
        self.time = kwargs['time']
        self.distance = kwargs['distance']

    def __repr__(self):
        return f"ID: {self.id} - " \
               f"Origin: {self.origin_airport} - " \
               f"Destination: {self.destination_airport} - " \
               f"Time: {self.time} - " \
               f"Distance: {self.distance}"


class Airline(db.Model):
    __tablename__ = 'airline'

    id = db.Column(db.String(10), primary_key=True)
    name = db.Column(db.String(256), nullable=False)

    def __init__(self, **kwargs):
        self.id = kwargs['id']
        self.name = kwargs['name']

    def __repr__(self):
        return f"ID: {self.id} - Name: {self.name}"


class Flight(db.Model):
    __tablename__ = 'flight'

    id = db.Column(db.String(32), primary_key=True)
    airline_id = db.Column(db.String(10), db.ForeignKey('airline.id', ondelete="CASCADE"), nullable=False)
    flight_number = db.Column(db.Integer, nullable=False)
    tail_number = db.Column(db.String(10), nullable=False)
    route_id = db.Column(db.String(10), db.ForeignKey('route.id', ondelete="CASCADE"), nullable=False)

    def __init__(self, **kwargs):
        self.id = kwargs['id']
        self.airline_id = kwargs['airline_id']
        self.flight_number = kwargs['flight_number']
        self.tail_number = kwargs['tail_number']
        self.route_id = kwargs['route_id']

    def __repr__(self):
        return f"ID: {self.id} - " \
               f"Airline: {self.airline_id} - " \
               f"Flight Number: {self.flight_number} - " \
               f"Tail Number: {self.tail_number} - " \
               f"Route ID: {self.route_id}"


OriginAirport = db.aliased(Airport, name='OriginAirport')
DestinationAirport = db.aliased(Airport, name='DestinationAirport')


def database_init_app(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()
