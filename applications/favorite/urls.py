from django.urls import path
from . import views


app_name = "favorite_app"

urlpatterns = [
    path('favorite/add/<pk>', views.AddFavoriteView.as_view(), name='add'),
    path('favorite/delete/<pk>', views.DeleteFavoriteView.as_view(), name='delete'),
]
