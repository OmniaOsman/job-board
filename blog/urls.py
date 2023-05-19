from django.urls import path 
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog, name='blog'),
    path('<slug:slug>/', views.post_details, name='post-details'),
    path('add-post', views.add_post, name='add-post'),
    path('<str:name>/', views.display_category, name='display-category'),
]
