from django.urls import path
from .import views


urlpatterns = [
    path('', views.dashboard, name='dashpage'),
    path('search/', views.search, name='searchpage'),
    path('upload/', views.upload, name='upload')

]