from django.urls import path, include
from . import views
from .views import *

urlpatterns = [
    #     path('', views.meterList, name='meterList'),
    path('', iViews.as_view(), name='iviews'),
    path('delete/<int:id>/', views.delete_items, name='delete_items'),
    #path('seriallist/<int:id>/', views.seriallist, name='seriallist'),
    #path('listofserials/<int:id>/',views.seriallist_data, name='listofserials'),
]