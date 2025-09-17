from django.urls import path
from users.views import Sign_Up, Log_In, Log_Out
urlpatterns = [
    path('sign-up/', Sign_Up, name='sing-up'),
    path('log-in/',Log_In,name='log-in'),
    path('log-out/',Log_Out, name='log-out')
    
]