from rest_framework.serializers import ModelSerializer
from .models import DriverRoute

class DriverRouteSerializer(ModelSerializer):
    class Meta:
        model = DriverRoute
        fields = '__all__'