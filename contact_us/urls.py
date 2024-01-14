from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .import views
router = DefaultRouter() #this is router

router.register('', views.ContactusViewset) #one-->antena
urlpatterns = [
    path('', include(router.urls)),
]