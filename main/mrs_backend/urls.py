from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name="home" ),
    path('recommend/movie/<int:movie_id>/', views.recommendMovie, name="recommendMovie"),
    path('recommend/tv/<int:tv_id>/', views.recommendTV, name="recommendTV"),
]
