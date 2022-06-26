import pytest

from starlink import Satellite, GroupOfSatellites, Operator, Overlord


class TestSatellite:
    def test_create_valid_satellite(self):
        satellite_one = Satellite(500.0, (50.4444, 120.666))
        assert satellite_one.altitude == 500
        assert satellite_one.coordinates == (50.4444, 120.666)
        assert satellite_one.solar_sail_on == False
        assert satellite_one.sattelite_on == True
        assert satellite_one.signal_transmit_on == False

    def test_create_satellite_with_wrong_coordinates(self):
        with pytest.raises(ValueError):
            satellite_one = Satellite(500.0, (100.0, 120.999))
    
    def test_create_satellite_with_wrong_altitude(self):
        with pytest.raises(ValueError):
            satellite_one = Satellite(-500.0, (50.4444, 120.666))


class TestGroupOfSatellites:
    def test_create_group_of_satellites(self):
        group = GroupOfSatellites()
        assert type(group) == GroupOfSatellites
        assert len(group.satellites) == 0

    def test_add_remove_satellites(self):
        group = GroupOfSatellites()
        satellite_one = Satellite(500.0, (50.4444, 120.666))
        satellite_two = Satellite(500.0, (50.47744, 119.666))
        group.add_satellite(satellite_one)
        group.add_satellite(satellite_two)
        assert len(group.satellites) == 2
        group.remove_satellite(satellite_one)
        assert len(group.satellites) == 1

    def test_group_handles_remove_when_satellite_not_found(self):
        group = GroupOfSatellites()
        satellite_one = Satellite(500.0, (50.4444, 120.666))
        satellite_two = Satellite(500.0, (50.47744, 119.666))
        group.add_satellite(satellite_one)
        removed = group.remove_satellite(satellite_two)
        assert removed is None

class TestOperator:
    pass

class TestOverlord:
    def test_create_overlord(self):
        overlord = Overlord("Genghis", "Khan")
        assert str(overlord) == "Overlord Genghis Khan"