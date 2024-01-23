from django.urls import path
from .views import volatility_calculator

urlpatterns = [
    path('', volatility_calculator),
]
