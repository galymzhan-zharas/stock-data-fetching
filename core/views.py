from django.http import HttpResponse
from django.shortcuts import render
from .models import Stock
import finnhub
import datetime
import json
# Create your views here.

# stock symbols, company profile (may get repetetive), stock quote 
# Microsoft, Apple, Google, Tesla, Meta, Netflix, Amazon, Nvidia, Intel, AMD

def fetch_current_data(request):
    stocks = Stock.objects.order_by('-id')[:10]
    return render(request, 'core/index.html', {'stocks':stocks, 'string':'Latest'})


def history(request, symbol):
    stocks = Stock.objects.filter(symbol=symbol)
    return render(request, 'core/index.html', {'stocks':stocks, 'string':symbol})