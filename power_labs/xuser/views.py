from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import status, permissions

from xauth import utils as xauth_utils

from xuser import serializers as user_serializers
from xuser import models as user_models
from xuser.responses import u_responses
from xuser import utils as xuser_utils


class UserViewSet(ModelViewSet):
   
    queryset = user_models.CustomUser.objects.all()
    serializer_class = user_serializers.ReadCustomUserSerializer
    write_serializer_class = user_serializers.RegisterCustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        
        return self.queryset.filter(user_name=self.request.user.user_name)
    
    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = self.permission_classes

        return [permission() for permission in permission_classes]
    
    def create(self, request, *args, **kwargs):
        try:
            req = self.write_serializer_class(data=request.data)
            req.is_valid(raise_exception=True)
        except Exception as e:
            return Response(
                data=u_responses.user_error_response(message=xuser_utils.handle_serializer_errors(serializer_error=req.errors)),
                status=status.HTTP_400_BAD_REQUEST,
            )

        is_user, user = req.create(validated_data=req.validated_data)
        if not is_user:
            return Response(
                data=u_responses.user_error_response(message=user),
                status=status.HTTP_400_BAD_REQUEST,
            )

        access_token = xauth_utils.encode_jwt(user)

        return_serializer = user_serializers.RegisterUserResponseSerializer(
            data={"access": access_token}
        )
        try:
            return_serializer.is_valid(raise_exception=True)
            success_response = {"message": "User created successfully", "data": return_serializer.data}
            return Response(
                data=u_responses.user_success_response(data=success_response),
                status=status.HTTP_201_CREATED,
            )
        except Exception as e:

            return Response(
                data=u_responses.user_error_response(message=xuser_utils.handle_serializer_errors(serializer_error=req.errors)),
                status=status.HTTP_400_BAD_REQUEST,
            )

    def list(self, request, *args, **kwargs):
    
        try:

            queryset = self.filter_queryset(self.get_queryset())

            serializer = self.get_serializer(queryset, many=True)

            success_response = {
                "message": "Successfully fetched users",
                "data": serializer.data,
            }
            return Response(
                data=u_responses.user_success_response(data=success_response),
                status=status.HTTP_200_OK,
            )
        except Exception as e:
            return Response(
                data=u_responses.user_error_response(message="Unauthenticated user"),
                status=status.HTTP_400_BAD_REQUEST,
            )

    def retrieve(self, request, *args, **kwargs):

        try:
            instance = self.get_object()
            serializer = self.serializer_class(instance)
            data = serializer.data

            success_response = {
                "message": "Successfully fetched user",
                "data": data
            }

            return Response(
                data=u_responses.user_success_response(data=success_response),
                status=status.HTTP_200_OK,
            )

        except Exception as e:
            return Response(
                data=u_responses.user_error_response(message="Unable to retrieve user"),
                status=status.HTTP_400_BAD_REQUEST,
            )
    
    def destroy(self, request, *args, **kwargs):

        try:
            instance = self.get_object()
        except Exception as get_instance_error:
           return Response(
                data=u_responses.user_error_response(message="Unable to get user profile"),
                status=status.HTTP_400_BAD_REQUEST,
            )
        
        instance.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)