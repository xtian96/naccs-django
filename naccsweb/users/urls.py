from django.urls import path

from . import views

urlpatterns = [
    path(r'users/<page_alias>', views.profile, name='profile'),
    path(r'register/', views.register, name='register'),
    path('activate/<slug:uidb64>/<slug:token>)/', views.activate, name='activate'),
    path(r'register/pending', views.pending, name='pending'),
    path(r'notfound/', views.not_found, name='not found')
]