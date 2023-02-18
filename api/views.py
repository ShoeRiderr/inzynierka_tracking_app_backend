from rest_framework.decorators import api_view
from rest_framework.response import Response
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
