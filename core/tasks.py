from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from .models import Company, Stock
from celery import shared_task
import finnhub
import datetime

# Create your views here.

# stock symbols, company profile (may get repetetive), stock quote 

# Microsoft, Apple, Google, Tesla, Meta, Netflix, Amazon, Nvidia, Intel, AMD

@shared_task
def fetch_current_data():
    finnhub_client = finnhub.Client(api_key='chrislhr01qkb63avj10chrislhr01qkb63avj1g') #finnhub.Client(api_key=settings.FINNHUB_API_KEY) 
    stocks_symbols = ['MSFT', 'AAPL', 'GOOGL', 'TSLA', 'META', 'NFLX', 'AMZN', 'NVDA', 'INTC', 'AMD']
    for symbol in stocks_symbols: 
        company_profile = finnhub_client.company_profile2(symbol=symbol)
        company_obj = Company(**company_profile)
        company_obj.save()
        
        stock_quote = finnhub_client.quote(symbol)
        stock = {'company_profile':company_obj, 'symbol':symbol, 'time':datetime.datetime.now()}
        stock.update(stock_quote)
        obj = Stock(**stock)
        obj.save()

