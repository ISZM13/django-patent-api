from django.urls import path
from . import views

urlpatterns = [
    path("patents/", views.PatentListCreate.as_view(), name="patent-view-create"),
    path("patents/<str:patent_id>/", views.PatentRetrieveUpdateDestroy.as_view(), name="patent-detail"),
]
