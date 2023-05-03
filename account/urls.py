from django.urls import path
from .views import index,register,Login_user


urlpatterns = [
    path('', index, name='auth'),
    path ('register/', register, name='register'),
    path ('login', Login_user, name='login' )
]
