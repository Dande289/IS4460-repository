from django.urls import path
from . import views
from .views import ShowListCreateView, ShowDetailView, UserListCreateView, UserDetailView

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    #/website/ urls
    path('list/', views.ShowList.as_view(),name ='show-list'),
    path('edit/<int:show_id>/', views.ShowEdit.as_view(), name ='show-edit'),
    path('add/', views.ShowAdd.as_view(),name ='show-add'),
    path('details/<int:show_id>/',views.ShowDetails.as_view(),name ='show-details'),
    path('show_delete/<int:show_id>/', views.ShowDelete.as_view(),name ='show-delete'),

    #/api/ urls
    path('show_detail/<int:pk>/', ShowDetailView.as_view(),name ='show-detail'),
    path('show_list/', ShowListCreateView.as_view(),name ='show-list-create'),

    path('users/', UserListCreateView.as_view(),name = 'user-list-create'),
    path('users/<int:pk>/', UserDetailView.as_view(),name = 'user-detail')

]