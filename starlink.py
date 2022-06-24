"""Create a system for the management and control of a system of satellites 
that will enable connection to the Internet from any place on the globe."""
from uuid import uuid4

class Satellite:
    def __init__(self, altitude: float, coordinates: tuple) -> None:
        """ Altitude - floating point in kilometers
            Coordinates - tuple of format (longitude: float, latitude: float)"""
        self.id = uuid4()
        self.altitude = altitude
        self.coordinates = coordinates
        self.solar_sail_on = False
        self.signal_transmit_on = False
        self.sattelite_on = False

    def __repr_(self):
        return f'Satellite id: {self.id}'
        


# It should have: uuid, altitude, coordinates, solar sail status(on/off), signal transmit status(on/off), satellite on status


class GroupOfSatellites:
    def __init__(self):
        self.satellites = set()

    def add_satellite(self, satellite: Satellite):
        self.satellites.add(satellite)

    def remove_satellite(self, satellite: Satellite):
        try:
            self.satellites.remove(satellite)
        except KeyError as err:
            print("Unable to remove - satellite not found in the group")

    def get_satellites(self):
        return self.satellites


# Contains a record of the satellites that are in a group


class Operator:
    def __init__(self, first_name, last_name):
        self.id = uuid4()
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return f'Operator {self.first_name} {self.last_name}'


# To have: first name, last name, uuid
# To be able to..:
# - change the elevation and coordinates of individual satellites
# - change the altitude and coordinates of a whole group
# - open and fold the sun sails for a single satellite and the whole group
# - turn on and off the broadcast signal for individual satellites and groups
# - can create new groups


class Overlord:
    ...


# Has to have: first name, last name, uuid
# It's got to be able to:
# - the same as a regular operator
# - can shut down individual satellites, selected groups or the whole system (all available satellites)
