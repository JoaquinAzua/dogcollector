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
    path('dogs/<int:dog_id>/add_feeding/', views.add_feeding, name='add_feeding'),

    # 'dogs/<int:dog_id>/assoc_toy/<int:toy_id>/' - Associating toy to dog by id
    path('dogs/<int:dog_id>/assoc_toy/<int:toy_id>/', views.assoc_toy, name='assoc_toy'),
    
    # 'toys/' - Toy Index Route(listview)
    path('toys/', views.ToyList.as_view(), name='toys_index'),

    # 'toys/<int:pk>/' - Toys Detail Route
    path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toys_detail'),

    # 'toys/create/' - Toys Create Route
    path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),

    #  toys/<int:pk>/update/' - Toys Update Route
    path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toys_update'),

    # toys/<int:pk>/delete/' - Toys Delete Route
    path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toys_delete'),


]