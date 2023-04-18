from django.shortcuts import render
from costing.models import *
from django.http import JsonResponse
from datetime import datetime,timedelta

# Create your views here.
def index(request):
    return render(request, 'monthlyCost/dashboard.html')

def get_cost_data(request):
    date = request.GET.get("date")
    month, year = date.split()
    month = int(month)
    year = int(year)
    start_date = datetime(year, month, 1)
    if(month == 12):
        end_date = datetime(year+1, 1, 1) - timedelta(days=1)
    else:
        end_date = datetime(year, month + 1, 1) - timedelta(days=1)
    costings = Costing.objects.filter(Date__range=[start_date, end_date]).values()
    return JsonResponse({"data": list(costings)})