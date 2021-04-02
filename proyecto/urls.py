
from django.contrib import admin
from django.urls import path,include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers
from productos import views


urlpatterns = [
    path('productos/', views.customer_list.as_view()),
    path('productos/<int:pk>/',views.detail_product.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)