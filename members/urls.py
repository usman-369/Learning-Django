from django.urls import path, include
from . import views

from rest_framework.routers import DefaultRouter
from .views import ContactBookViewSet

router = DefaultRouter()
router.register(r'contact-book', ContactBookViewSet)

urlpatterns = [
    path('', views.main, name='main'),
    path('members/', views.members, name='members'),
    path('members/details/<slug:slug>', views.details, name='details'),
    path('testing/', views.testing, name='testing'),
    path('', include(router.urls)),
]
