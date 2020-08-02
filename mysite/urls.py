from django. urls import path
from . import views


urlpatterns = [
    path('', views.index, name='base'),
    path('head/', views.index, name='head'),
    path('poslug/', views.poslug, name='poslug'),
    path('info/', views.info, name='info'),
    path('kontakt/', views.kontakt, name='kontakt'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('price/', views.price, name='price'),
]