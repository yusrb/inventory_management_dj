from django.urls import path
from .views import (
  index,
  staff,
  staff_detail,
  product,
  product_del,
  product_update,
  order,
)

urlpatterns = [
  path('dashboard/', index , name="dashboard_index"),
  path('staff/', staff, name="dashboard_staff"),
  path('staff/detail/<int:pk>', staff_detail, name="dashboard_staff_detail"),
  path('product/', product, name="dashboard_product"),
  path('product/delete/<int:pk>', product_del, name="dashboard_product_delete"),
  path('product/update/<int:pk>', product_update, name="dashboard_product_update"),
  path('order/', order, name="dashboard_order")
]