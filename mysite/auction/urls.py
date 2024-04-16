from django.urls import path, include
from .views import*

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('car/', CarViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='car_list'),
    path('car/<int:pk>/',
         CarViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='car_detail'),

    path('bet/', BetViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='bet_list'),
    path('bet/<int:pk>/', BetViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='bet_detail'),
]
