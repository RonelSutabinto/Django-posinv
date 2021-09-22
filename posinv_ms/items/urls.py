from django.urls import path, include
from . import views
from .views import *

urlpatterns = [
    #     path('', views.meterList, name='meterList'),
    path('', iViews.as_view(), name='iviews'),
    path('delete/<int:iditems>/', views.delete_items, name='delete_items'),
    
    #path('seriallist/<int:idmeters>/edit/<int:id>/',
    #     views.edit_meters, name='edit_meters'),

    #path('seriallist/<int:iditems>/', views.seriallist, name='seriallist'),
    #path('listofserials/<int:iditems>/',views.seriallist_data, name='listofserials'),
]