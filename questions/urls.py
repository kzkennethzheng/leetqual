from django.urls import path

from . import views

app_name = 'questions'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('tag/<int:pk>/', views.TagView.as_view(), name='tag'),
    path('random/', views.RandomView.as_view(), name='random'),
    path('search/', views.SearchResultsView.as_view(), name='search_results'),
    path('tag_list/', views.TagListView.as_view(), name='tag_list'),
]