from django.urls import path

from .views import (
    GoogleLoginView,
    GithubLoginView
)
urlpatterns = [
    path('google/', GoogleLoginView.as_view(), name='google_login'),
    path('github/', GithubLoginView.as_view(), name='github_login')
]