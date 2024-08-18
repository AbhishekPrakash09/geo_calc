from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer, CustomTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .search import search_location
from .calculate import calculate_distance

class UserCreateView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class GetLocationView(APIView):
    def get(self, request):
        start_location = request.query_params.get('start_location')
        destination_location = request.query_params.get('destination_location')

        if not start_location or not destination_location:
            return Response(
                {"error": "Both start_location and destination_location are required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        start_result = search_location(start_location)
        destination_result = search_location(destination_location)

        if start_result and destination_result:
            distance = calculate_distance(start_result, destination_result)
            return Response({
                'start_location': start_result,
                'destination_location': destination_result,
                'distance': distance
            }, status=status.HTTP_200_OK)
        else:
            return Response(
                {"error": "One or both locations could not be found."},
                status=status.HTTP_404_NOT_FOUND
            )