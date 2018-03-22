from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewset)
router.register(r'doctors', views.DoctorViewset)
router.register(r'doctor-categories', views.DoctorCategoryViewset)
router.register(r'tips', views.HealthTipViewset)
router.register(r'recommendations', views.DoctorRecommendationViewSet)

urlpatterns = [
    path('', include(router.urls)), path("bot/", views.BotView.as_view())
]
