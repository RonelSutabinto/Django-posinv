from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from posinv_ms .views import dashboard as home

from .views import *

urlpatterns = [
    # path('', LoginView.as_view(), name='login'),
    path('', login, name='login'),
    path('home', home, name='home'),
    path('regs', register, name='register'),
    path('logout', logout_view, name='logout'),

    # path('admin/', admin.site.urls),
]