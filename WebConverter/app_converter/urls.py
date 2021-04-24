from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('converterTo/', views.converterTo, name='converterTo'),
    path('', views.index, name='index'),
    path('add_data/', views.add_data, name='add_data'),
    path('search_data/', views.search_data, name='search_data'),
]


