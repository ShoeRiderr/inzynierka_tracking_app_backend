from django.urls import path
from . import views
from .views import UserRecordView

app_name = 'api'
urlpatterns = [
    path('drivers-routes/', views.driverRoutes),
    path('drivers-routes/<str:id>/', views.driverRoute),
    path('users/', UserRecordView.as_view(), name='users'),
]
