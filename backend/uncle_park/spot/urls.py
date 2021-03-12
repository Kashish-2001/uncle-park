from django.urls import path
from .views import *

urlpatterns = [
    path('spot/', spot_list),
    path('spot/<int:pk>', SpotDetail.as_view()),
]
