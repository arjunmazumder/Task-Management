from django.urls import path
from core.views import no_permission
urlpatterns = [
    path('no-permission/', no_permission, name='no-permission')
    
]