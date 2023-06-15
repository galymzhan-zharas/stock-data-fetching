import os # why import OS?
from celery import Celery 

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stock_market.settings') #what does it do?

app = Celery('stock_market')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
