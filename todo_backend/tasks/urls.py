# tasks/urls.py
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)  # Enregistre le viewset de 'tasks'

urlpatterns = router.urls  # Assure-toi que l'URL du routeur est utilisée
