from django.urls import path

from . import views

urlpatterns = [
    path('', views.titre_index, name='titre_index'),
    # path('get/<str:value>', views.get_header, name='process'),
]