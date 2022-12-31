from django.urls import path

from .views import log_in, log_out, sign_up

urlpatterns = [
    path('login/', log_in),
    path('logout/', log_out),
    path('signup/', sign_up)
]
