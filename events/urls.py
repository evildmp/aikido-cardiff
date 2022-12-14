from django.urls import path

from . import views


app_name = 'events'
urlpatterns = [
    path('', views.EventsView.as_view(), name='index'),
    path('<slug:slug>/', views.DetailView.as_view(), name='detail'),
]
