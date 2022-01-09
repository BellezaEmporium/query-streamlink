from django.urls import path
from .app import app

urlpatterns = [
    path("", app.urls),
]