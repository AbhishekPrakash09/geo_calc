from django.urls import reverse
from rest_framework.test import APITestCase, APIRequestFactory, force_authenticate
from rest_framework import status
from geo_calc_app.models import Location
from geo_calc_app.documents import LocationDocument
from geo_calc_app.views import GetLocationView
from django.contrib.auth.models import User


class ApplicationTests(APITestCase):

    def setUp(self):

        self.register_url = reverse('user_register')
        self.login_url = reverse('token_obtain_pair')

        self.user = User.objects.create_user(
            username='test@gmail.com', 
            email='test@gmail.com', 
            password='testpassword'
        )
        
        self.location1 = Location.objects.create(
            formatted_address="Spectra Cypress, Varthur Main Rd, Thubarahalli, Brookefield, Bengaluru, Karnataka 560066, India",
            latitude=12.955905,
            longitude=77.71736
        )
        self.location2 = Location.objects.create(
            formatted_address="8500 Beverly Blvd, Los Angeles, CA 90048, USA",
            latitude=34.0751706,
            longitude=-118.3773546
        )

        LocationDocument().update(self.location1)
        LocationDocument().update(self.location2)


    def test_registration_missing_parameters(self):

        response = self.client.post(self.register_url, data={})

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    
    def test_authentication_sucess(self):

        response = self.client.post(self.login_url, data={
            'username': 'test@gmail.com',
            'password': 'testpassword'
        }, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_get_location_distance(self):

        factory = APIRequestFactory()  

        data = {
            'start_location': 'Spectra Cypress',
            'destination_location': 'Beverly Centre',
        }

        request = factory.get('calc-distance', data)
        force_authenticate(request, user=self.user)
        
        view = GetLocationView.as_view()

        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        self.assertIn('start_location', response.data)
        self.assertIn('destination_location', response.data)
        self.assertIn('distance', response.data)
        
        self.assertAlmostEqual(response.data['distance'], 14515.25, places=2)

    def test_missing_parameters(self):

        factory = APIRequestFactory()  

        data = {
            'destination_location': 'Beverly Centre',
        }

        request = factory.get('calc-distance', data)
        force_authenticate(request, user=self.user)
        
        view = GetLocationView.as_view()

        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    def test_invalid_location(self):

        factory = APIRequestFactory()  

        data = {
            'start_location': 'invalid location',
            'destination_location': 'beverly centre',
        }

        request = factory.get('calc-distance', data)
        force_authenticate(request, user=self.user)
        
        view = GetLocationView.as_view()

        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

  
   
