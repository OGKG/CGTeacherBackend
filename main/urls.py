from django.urls import path, include
from .views import UserViewSet, UniversityGroupViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('groups', UniversityGroupViewSet)

urlpatterns = [
    # path('current_user/', current_user),
    # path('users/', UserList.as_view()),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
