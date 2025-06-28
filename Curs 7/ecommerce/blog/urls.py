from django.urls import path
from .views import blog_details_view, blog_list_view, blog_details_view_with_slug

urlpatterns = [
    path("all", blog_list_view),
    path("details/<int:blogid>", blog_details_view),
    path("details/<slug>", blog_details_view_with_slug)
]
