from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from .models import Wallet
from datetime import datetime
from django.shortcuts import render
from django.utils import timezone

def current_coins(request):
    wallet = Wallet.objects.first()
    if wallet is None:
        wallet = Wallet.objects.create(coins=1000)
    return JsonResponse({"Current balance in wallet is" : wallet.coins})


def start_timer(request):
    if request.method == 'POST':
         # Start the timer
        wallet = Wallet.objects.first()
        if wallet is None:
            wallet = Wallet.objects.create(coins=1000)

        # Start the timer with the current time in the server's timezone
        wallet.start_time = timezone.now()
        wallet.save()

        return JsonResponse({'status': 'Timer started successfully.'})
    else:
        return render(request, 'wallet/start_timer.html')

def stop_timer(request):
    if request.method == 'POST':
        try:
            wallet = Wallet.objects.first()
            if wallet is None:
                return JsonResponse({'error': 'Wallet not found.'}, status=404)

            # Convert start_time and current_time to the same timezone
            if wallet.start_time is not None : start_time = wallet.start_time.astimezone(timezone.get_current_timezone())
            else: return render(request, 'wallet/start_timer.html')
            current_time = timezone.now()

            # Calculate remaining balance
            duration = (current_time - start_time).total_seconds() / 60  # minutes
            print("time : ", duration)
            coins_deducted = int(duration) * 10
            remaining_balance = wallet.coins - coins_deducted

            # Stop the timer and update balance
            wallet.start_time = None
            wallet.coins = remaining_balance
            wallet.save()

            return JsonResponse({'status': 'Timer stopped successfully.', 'balance': remaining_balance})
        except ObjectDoesNotExist:
            return JsonResponse({'error': 'Wallet not found.'}, status=404)
    else:
        return render(request, 'wallet/stop_timer.html')