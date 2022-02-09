from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_list, name='user_list'),
    path('user/<int:pk>', views.user_details, name='user_details'),
    path('user/new', views.user_create, name='user_create'),
    path('user/<int:pk>/edit', views.user_edit, name='user_edit'),
    path('user/<int:pk>/delete', views.user_delete, name='user_delete'),

    path('movie/', views.movie_list, name='movie_list'),
    path('movie/<int:pk>', views.movie_details, name='movie_details'),
    path('movie/new', views.movie_create, name='movie_create'),
    path('movie/<int:pk>/edit', views.movie_edit, name='movie_edit'),
    path('movie/<int:pk>/delete', views.movie_delete, name='movie_delete'),

    path('role/', views.role_list, name='role_list'),
    path('role/<int:pk>', views.role_details, name='role_details'),
    path('role/new', views.role_create, name='role_create'),
    path('role/<int:pk>/edit', views.role_edit, name='role_edit'),
    path('role/<int:pk>/delete', views.role_delete, name='role_delete'),

    path('actor/', views.actor_list, name='actor_list'),
    path('actor/<int:pk>', views.actor_details, name='actor_details'),
    path('actor/new', views.actor_create, name='actor_create'),
    path('actor/<int:pk>/edit', views.actor_edit, name='actor_edit'),
    path('actor/<int:pk>/delete', views.actor_delete, name='actor_delete'),

    
    path('vote/', views.vote_list, name='vote_list'),
    path('vote/<int:pk>', views.vote_details, name='vote_details'),
    path('vote/new', views.vote_create, name='vote_create'),
    path('vote/<int:pk>/delete', views.vote_delete, name='vote_delete'),

    path('comment/', views.comment_list, name='comment_list'),
    path('comment/<int:pk>', views.comment_details, name='comment_details'),
    path('comment/new', views.comment_create, name='comment_create'),
    path('comment/<int:pk>/edit', views.comment_edit, name='comment_edit'),
    path('comment/<int:pk>/delete', views.comment_delete, name='comment_delete'),






]