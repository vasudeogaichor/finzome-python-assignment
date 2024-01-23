import pandas as pd
import numpy as np
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_POST

def process_data(data):
    """
    Process the input DataFrame to calculate daily and annualized volatility.

    Parameters:
    - data (pd.DataFrame): Input DataFrame with columns ['date', 'open', 'high', 'low', 'close', 'shares_traded', 'turnover'].

    Returns:
    - Tuple(float, float): Tuple containing daily_volatility and annualized_volatility.
    """
    column_names = ['date', 'open', 'high', 'low', 'close',
                    'shares_traded', 'turnover']
    data.columns = column_names
    data['daily_returns'] = (data['close'] / data['close'].shift(1)) - 1
    daily_volatility = np.std(data['daily_returns'])
    annualized_volatility = daily_volatility * np.sqrt(len(data))
    return daily_volatility, annualized_volatility


@csrf_protect
@require_POST
def calculate_volatility(request):
    """
    View function to calculate and return daily and annualized volatility based on the uploaded CSV file.

    Parameters:
    - request (HttpRequest): The HTTP request object containing the uploaded CSV file.

    Returns:
    - JsonResponse: JSON response containing daily_volatility and annualized_volatility.
    """
    csv_obj = request.FILES['file']
    data = pd.read_csv(csv_obj, header=0)
    daily_volatility, annualized_volatility = process_data(data)
    return JsonResponse({'daily_volatility': daily_volatility,
                          'annualized_volatility': annualized_volatility
                          })
