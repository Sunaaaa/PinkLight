from django.urls import path
from . import views

app_name = 'webserver'
urlpatterns = [
    path('', views.index, name="index"),
    path('new/', views.new, name="new"),
    path('<int:train_pk>/', views.detail, name="detail"),
    path('<int:train_pk>/edit/', views.edit, name="edit"),
]
