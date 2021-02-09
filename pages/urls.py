from django.urls import path
from .views import home_page_view, otra_prueba

urlpatterns = [
    path('', home_page_view, name='home'),
    path('about', otra_prueba, name='about'),

]
