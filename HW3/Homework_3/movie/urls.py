#urls.py
from django.urls import path
from . import views
from .views import MovieListCreateView, MovieDetailView, UserListCreateView, UserDetailView

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('list/', views.MovieList.as_view(),name ='movie-list'),
    path('edit/<int:movie_id>/', views.MovieEdit.as_view(), name ='movie-edit'),
    path('add/', views.MovieAdd.as_view(),name ='movie-add'),
    path('details/<int:movie_id>/',views.MovieDetails.as_view(),name ='movie-details'),
    path('movie_delete/<int:movie_id>/', views.MovieDelete.as_view(),name ='movie-delete'),


    path('movie_detail/<int:pk>/', MovieDetailView.as_view(),name ='movie-detail'),
    path('movie_list/', MovieListCreateView.as_view(),name ='movie-list-create'),

    path('users/', UserListCreateView.as_view(),name = 'user-list-create'),
    path('users/<int:pk>/', UserDetailView.as_view(),name = 'user-detail')

]