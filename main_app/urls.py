from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),

    # 'dogs/' - Dogs Index Route
    path('dogs/', views.dogs_index, name='dogs_index'),

    # 'dogs/<int:dog_id>/' - Dogs Detail Route
    path('dogs/<int:dog_id>/', views.dogs_detail, name='dogs_detail'),
]