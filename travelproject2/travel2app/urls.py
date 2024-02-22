from . import views
from django.urls import path

urlpatterns = [

    path('',views.demo,name='demo'),
    # path('arithmetic_operations/',views.arithmetic_operations,name='arithmetic_operations'),


]