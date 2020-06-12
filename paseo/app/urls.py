from django.urls import path
from . import views
urlpatterns = [
    path('', views.inicial, name='inicial'),
    path('sobre-nos/', views.sobre, name='sobre'),
    path('login/', views.log, name='login'),
]

