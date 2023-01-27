
from django.urls import path
from .views import Signup_view, Login_view, Logout_view

urlpatterns = [
    path('spv/', Signup_view.as_view(), name='signup_url'),
    path('log/',Login_view.as_view(), name='login_url'),
    path('lot/', Logout_view.as_view(), name='logout_url')
]
