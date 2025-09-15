from django.urls import path
from django.contrib import admin
from django.urls import path,include
from debug_toolbar.toolbar import debug_toolbar_urls
from core.views import home_page
urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', include("tasks.urls")),
    path('users/', include("users.urls")),
    path('core/', include("core.urls")),
    path('', home_page, name="homepage")
]+debug_toolbar_urls()
