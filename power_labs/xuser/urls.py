from rest_framework import routers

from xuser import views as user_views

router = routers.DefaultRouter()

router.register(r"account", user_views.UserViewSet, basename="account")

urlpatterns = []

urlpatterns += router.urls
