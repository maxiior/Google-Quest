from django.urls import path
from .views import make_prediction

app_name = 'urls'

urlpatterns = [
     path('predictions/', make_prediction, name='make_prediction'),
]