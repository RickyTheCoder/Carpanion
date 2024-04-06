from django.urls import path
from .views import (
    ApplicationView,
    AuthorizeUserWithApplication,
    LoginView
)

urlpatterns = [
    path('client/<str:id>/', ApplicationView.as_view(), name='application'),
    path('authorize/', AuthorizeUserWithApplication.as_view()),
    path('login/', LoginView.as_view(), name='login')
]