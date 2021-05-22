from django.urls import path
from .views import UserRejestracjaView, LoginView
from .forms import LoginForm
urlpatterns = [
    path('rejestracja/', UserRejestracjaView.as_view(), name="rejestracja"),
]
