from django.urls import path

from . import views
from .decorators import logout_required

urlpatterns = [
    path(r'users/<page_alias>', views.profile, name='profile'),
    path(r'register/', logout_required(views.register), name='register'),
    path('activate/<slug:uidb64>/<slug:token>)/', logout_required(views.activate), name='activate'),
    path(r'register/pending', logout_required(views.pending), name='pending_confirmation'),
    path(r'notfound/', logout_required(views.not_found), name='not found')
]