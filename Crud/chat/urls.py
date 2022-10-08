from django.urls import path
from . import views

urlpatterns = [
    path('', views.client),
    path('friend/<str:pk>', views.detail, name="friend")
]
