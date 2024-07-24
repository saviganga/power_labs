from django.db import models
import uuid

from sensors import enums as sensor_enums


class SensorData(models.Model):

    id = models.UUIDField(
        help_text="Unique sensor data identifier",
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    vehicle_id = models.CharField(max_length=6, help_text='vehicle unique reference')
    timestamp = models.DateTimeField(auto_now_add=True)
    sensor_type = models.CharField(max_length=6, help_text='sensor type')
    sensor_value = models.CharField(max_length=100, help_text='sensor value')

    class Meta:
        ordering = ['-timestamp']