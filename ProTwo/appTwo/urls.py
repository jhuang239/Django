from django.urls import path
from appTwo import views

urlpatterns = [
    path('', views.users, name='users'),  # URL for the users view of appTwo
]