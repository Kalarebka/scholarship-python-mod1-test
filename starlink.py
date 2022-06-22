"""Create a system for the management and control of a system of satellites 
that will enable connection to the Internet from any place on the globe."""


class Satellite:
    ...


# It should have: uuid, altitude, coordinates, solar sail status(on/off), signal transmit status(on/off), satellite on status


class GroupOfSatelites:
    ...


# Contains a record of the satellites that are in a group


class Operator:
    ...


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
