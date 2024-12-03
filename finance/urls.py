
from django.urls import path
from finance.views import HomeView, ChartView, ReceiveCsvView

app_name = 'finance'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('dashboard/', ChartView.as_view(), name='dashboard'),
    path('receive_csv/', ReceiveCsvView.as_view(), name='receive_csv')

]
