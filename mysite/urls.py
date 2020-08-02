from django. urls import path
from . import views


urlpatterns = [
    path('', views.index, name='base'),
    path('info/', views.info, name='info'),
    path('kontakt/', views.kontakt, name='kontakt'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('price/', views.price, name='price'),
]