from django.urls import path
from . import views
app_name="register"
urlpatterns=[
    path('',views.register,name="registerPage"),
    path('userregister',views.userregister,name="userregister"),
]