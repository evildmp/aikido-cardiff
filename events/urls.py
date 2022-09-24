from django.urls import path

from . import views


app_name = 'events'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('previous', views.IndexView.as_view(), name='previous'),
    path('<slug:slug>/', views.DetailView.as_view(), name='detail'),

]
