from django.urls import path
from . import views


urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='profile'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('taxauto/', views.taxauto, name='taxauto'),
    path('calculator/', views.calc, name='calculator')
]
