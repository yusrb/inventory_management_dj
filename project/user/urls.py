from django.urls import path
from .views import (
  # login,
  register,
  # logout
)

urlpatterns = [
  path('', register, name="register"),
]