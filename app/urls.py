from unicodedata import name
from django.db import router
from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from .views import GetUserAccount,UserCreateAPIView,TeamCreateAPIView


router = DefaultRouter()
router.register('user', GetUserAccount, basename='person')
router.register('useradd', UserCreateAPIView, basename='personadd')
router.register('teamadd', UserCreateAPIView, basename='team')

urlpatterns = [
    path ('', views.getName),
    path('teamadd/',TeamCreateAPIView.as_view(), name='teamadd'),
    path('user/', GetUserAccount.as_view(), name= 'user'),
    path('useradd/', UserCreateAPIView.as_view(), name= 'useradd'),
]