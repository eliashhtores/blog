from django.urls import path
from . import views


app_name = "home_app"

urlpatterns = [
    path('', views.HomePageView.as_view(), name='index'),
    path('register-subscriber', views.SubscriberCreateView.as_view(),
         name='register_subscriber'),
]
