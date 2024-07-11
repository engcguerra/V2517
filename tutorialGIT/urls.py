from django.urls import path
from . import views

app_name = "tutorialGIT"

urlpatterns = [
    path('', views.home, name='home'),
]
