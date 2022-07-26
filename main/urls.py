from django.urls import path, include
from rest_framework import routers
from .views import GrahamTaskAPIView, ModuleViewSet, TaskViewSet, UserViewSet, UniversityGroupViewSet, GrahamSchemaAPIView


router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('groups', UniversityGroupViewSet)
router.register('tasks', TaskViewSet)
router.register('modules', ModuleViewSet)

urlpatterns = [
    # path('current_user/', current_user),
    # path('users/', UserList.as_view()),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('graham-task/<int:id>', GrahamTaskAPIView.as_view()),
    path('graham-task/schema', GrahamSchemaAPIView.as_view())
]
