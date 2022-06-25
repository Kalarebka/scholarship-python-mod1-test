"""Create a system for the management and control of a system of satellites 
that will enable connection to the Internet from any place on the globe."""
from uuid import uuid4


class Satellite:
    """It should have: uuid, altitude, coordinates, solar sail status(on/off), signal transmit status(on/off), satellite on status"""
    instances = []

    def __init__(self, altitude: float, coordinates: tuple) -> None:
        """ Altitude - floating point in kilometers
            Coordinates - tuple of format (latitude: float, longitude: float)"""
        self.id = uuid4()
        self.altitude = altitude
        self.coordinates = coordinates
        self.solar_sail_on = False
        self.signal_transmit_on = False
        self.sattelite_on = False
        Satellite.instances.append(self)

    @property
    def altitude(self):
        return self._altitude

    @altitude.setter
    def altitude(self, value):
        """ It should probably have some smarter valid values, but I'm not a satellite expert ^^"""
        if value >= 0:
            self._altitude = value
        else:
            raise ValueError("Satellites won't fly undergroud ¯\\_(ツ)_/¯")

    @property
    def coordinates(self):
        return self._coordinates
    
    @coordinates.setter
    def coordinates(self, coords):
        lat, long = coords
        if -90 <= lat <= 90 and -180 <= long <= 180:
            self._coordinates = coords
        else:
            raise ValueError(f"Invalid coordinates provided: {coords}")

    def __repr__(self):
        return f'Satellite id: {self.id}'


class GroupOfSatellites:
    """Contains a record of the satellites that are in a group"""
    instances = []

    def __init__(self):
        self.satellites = set()
        GroupOfSatellites.append(self)

    def add_satellite(self, satellite: Satellite):
        self.satellites.add(satellite)

    def remove_satellite(self, satellite: Satellite):
        try:
            self.satellites.remove(satellite)
        except KeyError as err:
            print("Unable to remove - satellite not found in the group")

    def get_satellites(self):
        return self.satellites


class Operator:
    """To have: first name, last name, uuid
       To be able to..:
       - change the elevation and coordinates of individual satellites
       - change the altitude and coordinates of a whole group
       - open and fold the sun sails for a single satellite and the whole group
       - turn on and off the broadcast signal for individual satellites and groups
       - can create new groups"""
    def __init__(self, first_name, last_name):
        self.id = uuid4()
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return f'Operator {self.first_name} {self.last_name}'

    def set_satellite_altitude(self, satellite: Satellite, altitude):
        satellite.altitude(altitude)

    def set_group_altitude(self, group: GroupOfSatellites, altitude):
        for satellite in group.satellites:
            satellite.altitude(altitude)


class Overlord(Operator):
    """Has to have: first name, last name, uuid
       It's got to be able to:
       - the same as a regular operator
       - can shut down individual satellites, selected groups or the whole system (all available satellites)"""
    def shutdown_satellite(self, satellite: Satellite):
        pass

    def shutdown_group(self, satellite_group: GroupOfSatellites):
        pass

    def shutdown_all(self):
        pass
    