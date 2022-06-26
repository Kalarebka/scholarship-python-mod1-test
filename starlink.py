"""Create a system for the management and control of a system of satellites 
that will enable connection to the Internet from any place on the globe."""
import logging

from uuid import uuid4

# Set up logging instead of printing stuff
logging.basicConfig(filename='starlink_log.log', encoding='utf-8', level=logging.DEBUG)


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
        self.sattelite_on = True
        Satellite.instances.append(self)
        logging.info(f"Created {self}")

    @property
    def altitude(self):
        return self._altitude

    @altitude.setter
    def altitude(self, value):
        """ It should probably have some smarter valid values, but I'm not a satellite expert ^^"""
        if value >= 0:
            self._altitude = value
        else:
            logging.error(f"{self}: Altitude not set, invalid value")
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
            logging.error(f"{self}: coordinates not set, invalid values")
            raise ValueError(f"Invalid coordinates provided: {coords}")

    def __repr__(self):
        return f'Satellite id: {self.id}'


class GroupOfSatellites:
    """Contains a record of the satellites that are in a group"""
    instances = []

    def __init__(self):
        self.satellites = set()
        GroupOfSatellites.append(self)
        logging.info(f"Created new group of satellites")

    def add_satellite(self, satellite: Satellite):
        self.satellites.add(satellite)

    def remove_satellite(self, satellite: Satellite):
        try:
            self.satellites.remove(satellite)
            return satellite
        except KeyError as err:
            print("Unable to remove - satellite not found in the group")
            return None

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

    # Control satellite localization
    def set_satellite_altitude(self, satellite: Satellite, altitude):
        satellite.altitude(altitude)

    def set_group_altitude(self, group: GroupOfSatellites, altitude):
        for satellite in group.satellites:
            self.set_satellite_altitude(satellite, altitude)

    def change_satellite_coordinates(self, satellite: Satellite, delta_lat: float, delta_long: float):
        lat, long = satellite.coordinates
        new_lat = self.get_valid_lat(lat + delta_lat)
        new_long = self.get_valid_long(long + delta_long)
        satellite.coordinates((new_lat, new_long))

    def change_group_coordinates(self, group: GroupOfSatellites, delta_lat: float, delta_long: float):
        for satellite in group:
            self.change_satellite_coordinates(satellite, delta_lat, delta_long)

    # Control signal
    def satellite_signal_off(self, satellite: Satellite):
        satellite.signal_transmit_on = False

    def satellite_signal_on(self, satellite: Satellite):
        satellite.signal_transmit_on = True

    def group_signal_off(self, group: GroupOfSatellites):
        for satellite in group:
            self.satellite_signal_off(satellite)

    def group_signal_on(self, group: GroupOfSatellites):
        for satellite in group:
            self.satellite_signal_on(satellite)

    # Control sun sails
    def sun_sails_on(self, satellite: Satellite):
        satellite.solar_sail_on = True
    
    def group_sun_sails_on(self, group: GroupOfSatellites):
        for satellite in group.satellites():
            self.sun_sails_on(satellite)

    # Manage Groups
    def create_group(self):
        new_group = GroupOfSatellites()
        self.groups.append(new_group)
    
    # Helper methods
    def get_valid_lat(lat: float) -> float:
        pass

    def get_valid_long(long: float) -> float:
        pass


class Overlord(Operator):
    """Has to have: first name, last name, uuid
       It's got to be able to:
       - the same as a regular operator
       - can shut down individual satellites, selected groups or the whole system (all available satellites)"""
    def __repr__(self):
        return f"Overlord {self.first_name} {self.last_name}"

    def shutdown_satellite(self, satellite: Satellite):
        logging.info(f"{self}: shutting down {satellite}")
        satellite.sattelite_on = False

    def shutdown_group(self, satellite_group: GroupOfSatellites):
        for satellite in satellite_group:
            self.shutdown_satellite(satellite)

    def shutdown_all(self):
        for satellite in Satellite.instances:
            self.shutdown_satellite(satellite)
    