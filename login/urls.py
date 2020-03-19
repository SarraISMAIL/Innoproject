from django.urls import path
from . import views
app_name="login"
urlpatterns=[
    path('',views.log_in,name="loginPage"),
    path('userlogin',views.userlogin,name="userlogin"),
    path('userlogout',views.userlogout,name="logout")
]