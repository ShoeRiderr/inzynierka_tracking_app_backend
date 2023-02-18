from django.urls import path
from . import views

urlpatterns = [
    path('drivers-routes/', views.driverRoutes),
    path('drivers-routes/<str:id>/', views.driverRoute)
]
