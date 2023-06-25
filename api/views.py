from time import time
from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from core.models import Stock
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from datetime import datetime
from .serializers import StockSerializer
import finnhub
import pytz


# Create your views here.

# stock symbols, company profile (may get repetetive), stock quote 
# Microsoft, Apple, Google, Tesla, Meta, Netflix, Amazon, Nvidia, Intel, AMD

# def fetch_current_data(request):
#     stocks = Stock.objects.order_by('-id')[:10]
#     return render(request, 'core/index.html', {'stocks':stocks, 'string':'Latest'})


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated]) 
def fetch_current_data(request):

    stocks = Stock.objects.order_by('-id')[:10]
    serialized_stocks = StockSerializer(stocks, many=True)
    
    return Response(serialized_stocks.data)

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated]) 
def history(request, symbol):

    tz = pytz.timezone('Asia/Almaty')
    from_date = request.GET.get('from')
    to_date = request.GET.get('to')
    from_date_datetime = timezone.make_aware(datetime.strptime(from_date, '%Y-%m-%dT%H:%M:%S'), tz)
    to_date_datetime = timezone.make_aware(datetime.strptime(to_date, '%Y-%m-%dT%H:%M:%S'), tz)
    stocks = Stock.objects.filter(time__range=[from_date_datetime, to_date_datetime], symbol=symbol)
    paginator = PageNumberPagination()
    paginator.page_size = 1
    pages = paginator.paginate_queryset(stocks, request)
    serialized_stocks = StockSerializer(pages, many=True)

    return paginator.get_paginated_response(serialized_stocks.data) 