from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('', views.UserList.as_view(), name='user_list'),
    path('users/<int:pk>', views.UserDetail.as_view(), name='user_details'),

    path('movies', views.MovieList.as_view(), name='movie_list'),
    path('movies/<int:pk>', views.MovieDetail.as_view(), name='movie_details'),

    path('roles', views.RoleList.as_view(), name='role_list'),
    path('roles/<int:pk>', views.RoleDetail.as_view(), name='role_details'),

    path('actors', views.ActorList.as_view(), name='actor_list'),
    path('actors/<int:pk>', views.ActorDetail.as_view(), name='actor_details'),

    path('votes', views.VoteList.as_view(), name='vote_list'),
    path('votes/<int:pk>', views.VoteDetail.as_view(), name='vote_details'),

    path('comments', views.CommentList.as_view(), name='comment_list'),
    path('comments/<int:pk>', views.CommentDetail.as_view(), name='comment_details'),


]