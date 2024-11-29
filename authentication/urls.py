from authentication.views import SignupView, CustomLoginView, logout_view
from django.urls import path

app_name = 'authentication'

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout')

]
