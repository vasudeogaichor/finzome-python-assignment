from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def volatility_calculator(request):
    """
    View function for the Volatility Calculator page.

    Parameters:
    - request (HttpRequest): The HTTP request object.

    Returns:
    - HttpResponse: Rendered HTML response.
    """
    return render(request, 'frontend/index.html')
