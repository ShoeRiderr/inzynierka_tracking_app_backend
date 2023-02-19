from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser
from django.contrib.auth.models import User
from rest_framework import status
from .serializers import UserSerializer
from .serializers import DriverRouteSerializer
from .models import DriverRoute

@api_view(['GET', 'POST'])
def driverRoutes(request):
    if request.method == 'POST':
        data = request.data

        driverRoute = DriverRoute.objects.create(
            body=data['body']
        )
        serializer = DriverRouteSerializer(driverRoute, many=False)
        return Response(serializer.data)

    driverRoutes = DriverRoute.objects.all()
    serializer = DriverRouteSerializer(driverRoutes, many=True)
    return Response(serializer.data)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def driverRoute(request, id):
    driverRoute = DriverRoute.objects.get(id=id)
    if request.method == 'GET':
        serializer = DriverRouteSerializer(driverRoute, many=False)
        return Response(serializer.data)
    elif request.method == 'PUT' or 'PATCH':
        serializer = DriverRouteSerializer(driverRoute, data=request.data)
        if serializer.is_valid():
            serializer.save()
    if request.method == 'DELETE':
        driverRoute.delete()
        return Response('Driver route is deleted.')

    return Response(serializer.data)

class UserRecordView(APIView):
    """
    API View to create or get a list of all the registered
    users. GET request returns the registered users whereas
    a POST request allows to create a new user.
    """
    permission_classes = [IsAdminUser]

    def get(self, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            {
                "error": True,
                "error_msg": serializer.error_messages,
            },
            status=status.HTTP_400_BAD_REQUEST
        )