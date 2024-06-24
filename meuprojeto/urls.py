# meuprojeto/urls.py
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from accounts.views import custom_logout





urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('events/', include('events.urls')),
    path('accounts/', include('accounts.urls')),
    path('', include('events.urls')),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('logout/', custom_logout, name='logout'),
    
    
]
