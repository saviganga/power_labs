from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.decorators import action

from sensors import models as sensor_models
from sensors import serializers as sensor_serializers
from sensors import filters as sensor_filters

from xuser import utils as xuser_utils
from xuser.responses import u_responses

class SensorDataViewSet(ModelViewSet):

    queryset = sensor_models.SensorData.objects.all()
    serializer_class = sensor_serializers.SensorDataSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_class = sensor_filters.SensorDataFilter

    def get_queryset(self):
        return self.queryset.all()
    
    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = self.permission_classes

        return [permission() for permission in permission_classes]
    
    def create(self, request, *args, **kwargs):

        serializer = self.serializer_class(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception as serializer_error:
            
            return Response(
                data=u_responses.user_error_response(message=xuser_utils.handle_serializer_errors(serializer_error=serializer.errors)),
                status=status.HTTP_400_BAD_REQUEST,
            )
        
        is_sensor_data, sensor_data = serializer.create(validated_data=serializer.validated_data)
        if not is_sensor_data:
            return Response(
                data=u_responses.user_error_response(message=sensor_data),
                status=status.HTTP_400_BAD_REQUEST,
            )
        success_response = {
            "message": "Successfully added sensor data",
            "data": sensor_data,
        }
        
        return Response(
                data=u_responses.user_success_response(data=success_response),
                status=status.HTTP_200_OK,
            )
    
    def list(self, request, *args, **kwargs):

        try:
            queryset = self.filter_queryset(self.get_queryset())
            page = self.paginate_queryset(queryset)
            if page is not None:
                serializer = self.serializer_class(queryset, many=True)
                return self.get_paginated_response(serializer.data)
            serializer = self.serializer_class(queryset, many=True)
            success_response = {
                "message": "Successfully fetched sensor data",
                "data": serializer.data
            }
            
            return Response(
                    data=u_responses.user_success_response(data=success_response),
                    status=status.HTTP_200_OK,
                )
        except Exception as e:
            return Response(
                data=u_responses.user_error_response(message="Unable to fetch sensor data"),
                status=status.HTTP_400_BAD_REQUEST,
            )
        
    @action(methods=["get"], detail=False)
    def health(self, request, pk=None):

        return Response(
                    data=u_responses.user_success_response(),
                    status=status.HTTP_200_OK,
                )



