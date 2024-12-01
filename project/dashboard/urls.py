from django.urls import path
from .views import (
  index,
  staff,
  product,
  order,
)

urlpatterns = [
  path('dashboard/', index , name="dashboard_index"),
  path('staff/', staff, name="dashboard_staff"),
  path('product/', product, name="dashboard_product"),
  path('order/', order, name="dashboard_order")
]