# posts/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('design/', views.design_page, name='design_page'),
    path('web_dev/', views.web_dev_page, name='web_dev'),
    path('mob_dev/', views.mob_dev_page, name='mob_dev'),
    path('marketing/', views.market_page, name='market'),
]
