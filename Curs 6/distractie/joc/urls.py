from django.urls import path
from .views import rock_paper_view

urlpatterns = [
    path('', rock_paper_view),
]