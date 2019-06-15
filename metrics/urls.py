
from . import views
from django.urls import path, include

app_name= 'metrics'
urlpatterns = [
path('', views.HomeView.as_view(), name='home'),
path('<str:scholar_url>/results/', views.ResultView.as_view(), name= 'results'),
]