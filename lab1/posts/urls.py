from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts_list),
]

urlpatterns = [
    path('', views.posts_list, name="posts"),
]
urlpatterns = [
    path('', views.posts_list, name="posts"),
    path('<slug:slug>', views.post_page, name="page")
]

app_name = 'posts'

urlpatterns = [
    path('', views.posts_list, name="list"),
    path('new-post/', views.post_new, name='new-post'),
    path('<slug:slug>', views.post_page, name="page")
]
