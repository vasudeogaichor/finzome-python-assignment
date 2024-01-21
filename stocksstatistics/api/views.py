import pandas as pd
import numpy as np
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

def process_data(data):
    column_names = ['date', 'open', 'high', 'low', 'close',
                    'shares_traded', 'turnover']
    data.columns = column_names
    daily_volatility = np.std(data['daily_returns'])
    annualized_volatility = daily_volatility * np.sqrt(len(data))
    return daily_volatility, annualized_volatility


@csrf_exempt
@require_POST
def calculate_volatility(request):
    file_obj = request.FILES['file']
    data = pd.read_csv(file_obj, header=0)
    daily_volatility, annualized_volatility = process_data(data)
    return JsonResponse({'daily_volatility': daily_volatility,
                          'annualized_volatility': annualized_volatility
                          })
