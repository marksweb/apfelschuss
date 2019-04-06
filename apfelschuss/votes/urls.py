from django.urls import path
from . import views

app_name = "votes"
urlpatterns = [
    path('', views.voting, name='voting'),
]
