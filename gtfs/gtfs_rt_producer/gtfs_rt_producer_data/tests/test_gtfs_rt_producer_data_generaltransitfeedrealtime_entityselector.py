"""
Test case for EntitySelector
"""

import os
import sys
import unittest

sys.path.append(os.path.realpath(os.path.join(os.path.dirname(__file__), '../src'.replace('/', os.sep))))

from gtfs_rt_producer_data.generaltransitfeedrealtime.entityselector import EntitySelector
from test_gtfs_rt_producer_data_generaltransitfeedrealtime_tripdescriptor import Test_TripDescriptor

class Test_EntitySelector(unittest.TestCase):
    """
    Test case for EntitySelector
    """

    def setUp(self):
        """
        Set up test case
        """
        self.instance = Test_EntitySelector.create_instance()

    @staticmethod
    def create_instance():
        """
        Create instance of EntitySelector for testing
        """
        instance = EntitySelector(
            agency_id='whmfidyrcnomgemxhrgm',
            route_id='hahqagnthtqbzvmnlbgm',
            route_type=int(40),
            trip=Test_TripDescriptor.create_instance(),
            stop_id='bdejicezfnzhqmfcagtc'
        )
        return instance

    
    def test_agency_id_property(self):
        """
        Test agency_id property
        """
        test_value = 'whmfidyrcnomgemxhrgm'
        self.instance.agency_id = test_value
        self.assertEqual(self.instance.agency_id, test_value)
    
    def test_route_id_property(self):
        """
        Test route_id property
        """
        test_value = 'hahqagnthtqbzvmnlbgm'
        self.instance.route_id = test_value
        self.assertEqual(self.instance.route_id, test_value)
    
    def test_route_type_property(self):
        """
        Test route_type property
        """
        test_value = int(40)
        self.instance.route_type = test_value
        self.assertEqual(self.instance.route_type, test_value)
    
    def test_trip_property(self):
        """
        Test trip property
        """
        test_value = Test_TripDescriptor.create_instance()
        self.instance.trip = test_value
        self.assertEqual(self.instance.trip, test_value)
    
    def test_stop_id_property(self):
        """
        Test stop_id property
        """
        test_value = 'bdejicezfnzhqmfcagtc'
        self.instance.stop_id = test_value
        self.assertEqual(self.instance.stop_id, test_value)
    