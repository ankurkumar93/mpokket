from django.contrib import admin
from django.urls import path, include
from .views import GetUserView, Home

urlpatterns = [
    path('', Home.as_view(), name="get user view"),

    path('getuserview/<int:id>/', GetUserView.as_view(), name="get user view"),
    path('getuserview/<int:id>/<str:fmt>/', GetUserView.as_view(), name="get user view"),
]
