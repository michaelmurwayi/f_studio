from django.urls import path, include
from django.contrib import admin
from .views import *
from website import views

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('blog/', BlogView.as_view(), name="blog"),
    path('bookings/', BookView.as_view(), name="bookings"),
    path('classes/', ClassView.as_view(), name="classes")

]
