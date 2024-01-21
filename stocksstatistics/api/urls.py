from django.urls import path
from .views import calculate_volatility

urlpatterns = [
    path('calculate-volatility/', calculate_volatility),
]
