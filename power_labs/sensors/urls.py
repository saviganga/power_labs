from rest_framework import routers

from sensors import views as sensor_views

router = routers.DefaultRouter()

router.register(r"sensor-data", sensor_views.SensorDataViewSet, basename="sensor-data")

urlpatterns = []

urlpatterns += router.urls
