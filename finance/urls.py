
from django.urls import path
from finance.views import HomeView, ChartView

app_name = 'finance'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('dashboard/', ChartView.as_view(), name='dashboard'),

]
