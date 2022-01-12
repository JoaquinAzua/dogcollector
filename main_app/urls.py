from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),

    # 'dogs/' - Dogs Index Route
    path('dogs/', views.dogs_index, name='dogs_index'),

    # 'dogs/<int:dog_id>/' - Dogs Detail Route
    path('dogs/<int:dog_id>/', views.dogs_detail, name='dogs_detail'),

    # 'dogs/create/' - Dogs Create Route
    path('dogs/create/', views.DogCreate.as_view(), name='dogs_create'),

    # 'dogs/<int:pk>/update/' - Dogs Update Route
    path('dogs/<int:pk>/update/', views.DogUpdate.as_view(), name='dogs_update'),

    # 'dogs/<int:pk>/delete/' - Dogs Delete Route
    path('dogs/<int:pk>/delete/', views.DogDelete.as_view(), name='dogs_delete'),

    # 'dogs/<int:cat_id>/add_feeding/', - Add Feeding Route
    path('dogs/<int:dog_id>/add_feeding/', views.add_feeding, name='add_feeding')

]