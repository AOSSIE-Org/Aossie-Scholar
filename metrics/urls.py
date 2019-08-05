
from . import views
from django.urls import path, include

app_name= 'metrics'
urlpatterns = [
path('', views.HomeView.as_view(), name='home'),
path('<str:scholar_url>/results/', views.ResultView.as_view(), name= 'results'),
path('info_page', views.InfoPageView.as_view(), name= 'info_page'),
path('search_results', views.SearchResultsView.as_view(), name='search_results')
]