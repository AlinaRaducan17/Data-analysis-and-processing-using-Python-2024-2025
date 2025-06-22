from django.urls import path
from .views import validare_cnp_view, rezultat_cnp_view

#URL Mic
urlpatterns = [
  path('cnp', validare_cnp_view),
  path('rezultat', rezultat_cnp_view)
]
