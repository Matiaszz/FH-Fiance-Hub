
from django.urls import path
from finance.views import HomeView

app_name = 'finance'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),

]
