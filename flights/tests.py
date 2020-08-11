from django.test import Client ,TestCase

from .models import *

# Create your tests here.
class FlightTestCase(TestCase):

        def setUp(self):

        #create airports.
            a1=Airport.objects.create(code="AAA",city="city A")
            a2=Airport.objects.create(code="BBB",city="city B")

            #create Flights.
            Flights.objects.create(origin=a1, destination=a2, duration=100)
            Flights.objects.create(origin=a1, destination=a1, duration=200)
            Flights.objects.create(origin=a1, destination=a2, duration=-100)

        def test_departures_count(self):
            a=Airport.objects.get(code="AAA")
            self.assertEqual(a.Departures.count(),3)

        def  test_arrivals_count(self):
            a=Airport.objects.get(code="AAA")
            self.assertEqual(a.Arrivals.count(),1)

        def test_valid_flight(self):
            a1=Airport.objects.get(code="AAA")
            a2=Airport.objects.get(code="BBB")
            f=Flights.objects.get(origin=a1, destination=a2, duration=100)
            self.assertTrue(f.is_valid_flight())

        def test_valid_destination(self):
            a1=Airport.objects.get(code="AAA")
            f=Flights.objects.get(origin=a1, destination=a1)
            self.assertFalse(f.is_valid_flight())

        def test_invalid_flight_duration(self):
            a1=Airport.objects.get(code="AAA")
            a2=Airport.objects.get(code="BBB")
            f=Flights.objects.get(origin=a1, destination=a2, duration=-100)
            self.assertFalse(f.is_valid_flight())
            
        def test_index(self):
            c=Client()
            response=c.get("/flights/")
            self.assertEqual(response.status_code,200)
            self.assertEqual(response.context["flights"].count(),3)

      
