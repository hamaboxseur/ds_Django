# todo_backend/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('tasks.urls')),  # Assurez-vous que le fichier urls.py de 'tasks' est bien inclus
]
