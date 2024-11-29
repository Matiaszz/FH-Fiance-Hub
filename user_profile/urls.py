from user_profile.views import temp_view
from django.urls import path

app_name = 'user_profile'

urlpatterns = [
    path('', temp_view, name='profile'),
]
