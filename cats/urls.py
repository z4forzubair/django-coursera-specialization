from django.urls import path

from cats import views

app_name = 'cats'
urlpatterns = [
    path('', views.CatList.as_view(), name='all'),
    path('cats/create/', views.CatCreate.as_view(), name='cat_create'),
    path('cats/<int:pk>/update/', views.CatUpdate.as_view(), name='cat_update'),
    path('cats/<int:pk>/delete/', views.CatDelete.as_view(), name='cat_delete'),

    path('breeds/', views.BreedList.as_view(), name='breed_list'),
    path('breeds/create/', views.BreedCreate.as_view(), name='breed_create'),
    path('breeds/<int:pk>/update/', views.BreedUpdate.as_view(), name='breed_update'),
    path('breeds/<int:pk>/delete/', views.BreedDelete.as_view(), name='breed_delete'),
]
