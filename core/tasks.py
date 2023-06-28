from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from .models import Company, Stock
from celery import shared_task
import datetime, requests

# Create your views here.

# stock symbols, company profile (may get repetetive), stock quote 

# Microsoft, Apple, Google, Tesla, Meta, Netflix, Amazon, Nvidia, Intel, AMD

@shared_task
def fetch_current_data(request):
    
    api_key='chrislhr01qkb63avj10chrislhr01qkb63avj1g' #finnhub.Client(api_key=settings.FINNHUB_API_KEY) 
    base_url = 'https://finnhub.io/api/v1'
    company_profile_url = f'{base_url}/stock/profile2'
    stock_quote_url = f'{base_url}/quote'
    stocks_symbols = ['MSFT', 'AAPL', 'GOOGL', 'TSLA', 'META', 'NFLX', 'AMZN', 'NVDA', 'INTC', 'AMD']

    for symbol in stocks_symbols:
        try:
            params = {'symbol':symbol, 'token':api_key}
            company_profile = requests.get(company_profile_url, params=params).json()
            company_obj = Company(**company_profile)
            company_obj.save()

            stock_quote = requests.get(stock_quote_url, params=params).json()
            stock = {'company_profile': company_obj, 'symbol': symbol, 'time': datetime.datetime.now()}
            stock.update(stock_quote)
            stock_obj = Stock(**stock)
            stock_obj.save()
        except requests.exceptions.RequestException as e:
            if e.response.status_code == 503: 
                return HttpResponse("503: server unavailable")
            else: 
                return HttpResponse("Error while processing the request")


