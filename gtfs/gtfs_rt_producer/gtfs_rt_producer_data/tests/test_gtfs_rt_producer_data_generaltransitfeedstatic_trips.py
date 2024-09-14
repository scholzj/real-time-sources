"""
Test case for Trips
"""

import os
import sys
import unittest

sys.path.append(os.path.realpath(os.path.join(os.path.dirname(__file__), '../src'.replace('/', os.sep))))

from gtfs_rt_producer_data.generaltransitfeedstatic.trips import Trips
from test_gtfs_rt_producer_data_generaltransitfeedstatic_calendardates import Test_CalendarDates
from test_gtfs_rt_producer_data_generaltransitfeedstatic_calendar import Test_Calendar
from test_gtfs_rt_producer_data_generaltransitfeedstatic_directionid import Test_DirectionId
from test_gtfs_rt_producer_data_generaltransitfeedstatic_bikesallowed import Test_BikesAllowed
from test_gtfs_rt_producer_data_generaltransitfeedstatic_wheelchairaccessible import Test_WheelchairAccessible

class Test_Trips(unittest.TestCase):
    """
    Test case for Trips
    """

    def setUp(self):
        """
        Set up test case
        """
        self.instance = Test_Trips.create_instance()

    @staticmethod
    def create_instance():
        """
        Create instance of Trips for testing
        """
        instance = Trips(
            routeId='glxiimtdikghqgfudfbr',
            serviceDates=Test_Calendar.create_instance(),
            serviceExceptions=[Test_CalendarDates.create_instance(), Test_CalendarDates.create_instance()],
            tripId='mvraemginomsxnmzqiuz',
            tripHeadsign='xssixytluxtnbjubwttm',
            tripShortName='meszfyvfbykrzexbbzib',
            directionId=Test_DirectionId.create_instance(),
            blockId='xahdvgwihewgxrlnnhtn',
            shapeId='yghxdchdfvffcijzhfwh',
            wheelchairAccessible=Test_WheelchairAccessible.create_instance(),
            bikesAllowed=Test_BikesAllowed.create_instance()
        )
        return instance

    
    def test_routeId_property(self):
        """
        Test routeId property
        """
        test_value = 'glxiimtdikghqgfudfbr'
        self.instance.routeId = test_value
        self.assertEqual(self.instance.routeId, test_value)
    
    def test_serviceDates_property(self):
        """
        Test serviceDates property
        """
        test_value = Test_Calendar.create_instance()
        self.instance.serviceDates = test_value
        self.assertEqual(self.instance.serviceDates, test_value)
    
    def test_serviceExceptions_property(self):
        """
        Test serviceExceptions property
        """
        test_value = [Test_CalendarDates.create_instance(), Test_CalendarDates.create_instance()]
        self.instance.serviceExceptions = test_value
        self.assertEqual(self.instance.serviceExceptions, test_value)
    
    def test_tripId_property(self):
        """
        Test tripId property
        """
        test_value = 'mvraemginomsxnmzqiuz'
        self.instance.tripId = test_value
        self.assertEqual(self.instance.tripId, test_value)
    
    def test_tripHeadsign_property(self):
        """
        Test tripHeadsign property
        """
        test_value = 'xssixytluxtnbjubwttm'
        self.instance.tripHeadsign = test_value
        self.assertEqual(self.instance.tripHeadsign, test_value)
    
    def test_tripShortName_property(self):
        """
        Test tripShortName property
        """
        test_value = 'meszfyvfbykrzexbbzib'
        self.instance.tripShortName = test_value
        self.assertEqual(self.instance.tripShortName, test_value)
    
    def test_directionId_property(self):
        """
        Test directionId property
        """
        test_value = Test_DirectionId.create_instance()
        self.instance.directionId = test_value
        self.assertEqual(self.instance.directionId, test_value)
    
    def test_blockId_property(self):
        """
        Test blockId property
        """
        test_value = 'xahdvgwihewgxrlnnhtn'
        self.instance.blockId = test_value
        self.assertEqual(self.instance.blockId, test_value)
    
    def test_shapeId_property(self):
        """
        Test shapeId property
        """
        test_value = 'yghxdchdfvffcijzhfwh'
        self.instance.shapeId = test_value
        self.assertEqual(self.instance.shapeId, test_value)
    
    def test_wheelchairAccessible_property(self):
        """
        Test wheelchairAccessible property
        """
        test_value = Test_WheelchairAccessible.create_instance()
        self.instance.wheelchairAccessible = test_value
        self.assertEqual(self.instance.wheelchairAccessible, test_value)
    
    def test_bikesAllowed_property(self):
        """
        Test bikesAllowed property
        """
        test_value = Test_BikesAllowed.create_instance()
        self.instance.bikesAllowed = test_value
        self.assertEqual(self.instance.bikesAllowed, test_value)
    
