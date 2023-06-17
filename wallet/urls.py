from django.urls import path
from wallet.views import start_timer, stop_timer, current_coins

urlpatterns = [
    path('', current_coins, name = 'current_coins'),
    path('start-timer/', start_timer, name='start_timer'),
    path('stop-timer/', stop_timer, name='stop_timer'),
]
