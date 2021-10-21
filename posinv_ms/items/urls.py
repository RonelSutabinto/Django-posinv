from django.urls import path, include
from . import views
from .views import *

urlpatterns = [
    #     path('', views.meterList, name='meterList'),
    path('', IIIViews.as_view(), name='iiiviews'),
    path('delete/<int:id>/', views.delete_items, name='delete_items'),    
    
    path('add', views.add_item, name='add'),
    #path('save_item',views.save_item, name='save_item'),
    path('updateitem/<int:id>/',views.edit_item, name='edit_item'),
]