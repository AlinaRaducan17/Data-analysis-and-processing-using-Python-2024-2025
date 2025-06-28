from django.urls import path
from .views import NUME_VIEW2_view
from .views import NUME_VIEW_view

urlpatterns = [

	path("NUME_URL", NUME_VIEW_view),
	path("NUME_URL2", NUME_VIEW2_view),
]
