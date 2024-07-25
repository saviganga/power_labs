import django_filters

from sensors import models as sensor_models

class SensorDataFilter(django_filters.FilterSet):
    vehicle_id = django_filters.CharFilter(lookup_expr='iexact')
    sensor_type = django_filters.CharFilter(lookup_expr='iexact')
    start_time = django_filters.DateTimeFilter(field_name='timestamp', lookup_expr='gte')
    end_time = django_filters.DateTimeFilter(field_name='timestamp', lookup_expr='lte')

    class Meta:
        model = sensor_models.SensorData
        fields = ['vehicle_id', 'sensor_type', 'start_time', 'end_time']

