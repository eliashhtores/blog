from django.urls import path
from . import views


app_name = "entry_app"

urlpatterns = [
    path('entry/list', views.EntryListView.as_view(),
         name='list'),
    path('entry/detail/<pk>', views.EntryDetailView.as_view(),
         name='detail'),
]
