from django.urls import path
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
    path('', views.SchoolListView.as_view(), name='list'),
    path('create/', views.SchoolCreateView.as_view(), name='create'),
    path('<int:pk>/', views.SchoolDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', views.SchoolUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.SchoolDeleteView.as_view(), name='delete'),
]
