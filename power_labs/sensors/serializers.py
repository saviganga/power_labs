from rest_framework import serializers
from decimal import Decimal

from sensors import models as sensor_models
from sensors import enums as sensor_enums


class SensorDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = sensor_models.SensorData
        fields = "__all__"

    def create(self, validated_data):

        # validate_vehicle_id
        if len(validated_data.get('vehicle_id').replace(" ", "")) != 6:
            return False, "Oops! Vehicle id must be 6 characters"

        # validate sensor types
        sensor_type = validated_data.get('sensor_type').upper()
        if sensor_type not in sensor_enums.SENSOR_TYPES:
            return False, f"Oops! {sensor_type} not valid"
        
        # validate sensor value
        sensor_value = validated_data.get('sensor_value').split(',')
        if sensor_type == "GPS":
            if len(sensor_value) != 2:
                return False, "Oops Invalid sensor value. Please pass in values in the format 'longitude,latitude'"
            else:
                sensor_value = ','.join(sensor_value).replace(" ", "")
        else:
            if len(sensor_value) != 1:
                return False, "Oops Invalid sensor value. Please pass in values in the format 'sensor_value'"
            else:
                sensor_value = sensor_value[0].replace(" ", "")
            if sensor_type == "FUEL":
                if Decimal(sensor_value) > Decimal('100'):
                    return False, "Oops! Fuel values cannot be greater than 100"
        
        validated_data['vehicle_id'] = validated_data.get('vehicle_id').replace(" ", "").upper()
        validated_data['sensor_value'] = sensor_value
        validated_data['sensor_type'] = sensor_type

        try:
            sensor_data = self.Meta.model.objects.create(**validated_data)
        except Exception as sensor_data_error:
            return False, "Unable to add sensor data"
        
        return True, SensorDataSerializer(sensor_data).data