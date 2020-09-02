from django.urls import path

from . import views

urlpatterns = [
    path('', views.article_index, name='index'),
    # path('', views.index, name='index'),
]