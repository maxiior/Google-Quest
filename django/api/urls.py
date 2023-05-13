from django.urls import path
from .views import predictions

app_name = 'urls'

urlpatterns = [
     path('predictions/', predictions, name='make_prediction'),
]