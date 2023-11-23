from . import views
from django.urls import path
from .views import profile_view

urlpatterns = [
    path('profile/', views.profile_view, name="profile"),
    path('signup/', views.Register.as_view(), name='sighup')
]