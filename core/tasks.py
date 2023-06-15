from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from .models import Stock
from celery import shared_task
import finnhub
import datetime

# Create your views here.

# stock symbols, company profile (may get repetetive), stock quote 

# Microsoft, Apple, Google, Tesla, Meta, Netflix, Amazon, Nvidia, Intel, AMD

@shared_task
def fetch_current_data():
    finnhub_client = finnhub.Client(api_key=settings.FINNHUB_API_KEY)
    stocks_symbols = ['MSFT', 'AAPL', 'GOOGL', 'TSLA', 'META', 'NFLX', 'AMZN', 'NVDA', 'INTC', 'AMD']
    for symbol in stocks_symbols: 
        stock_quote = finnhub_client.quote(symbol) #a dictionary
        stock = {'symbol':symbol, 'time':datetime.datetime.now()}
        stock.update(stock_quote)
        obj = Stock(**stock)
        obj.save()

