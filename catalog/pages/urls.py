from django.urls import path
from . import views #aynı dizinin içinde old.dan nokta

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about')
]