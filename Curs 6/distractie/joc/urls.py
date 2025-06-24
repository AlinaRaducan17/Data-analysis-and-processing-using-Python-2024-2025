from django.urls import path
from .views import rock_paper_view, rock_paper_scissor_lizzard_spock_view

urlpatterns = [
    path('clasic', rock_paper_view),
    path('frumos',rock_paper_scissor_lizzard_spock_view),
]