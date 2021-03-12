from django.urls import path
from .views import *

urlpatterns = [
    path('users/', user_list),
    path('users/<int:pk>', UserDetail.as_view()),
]
