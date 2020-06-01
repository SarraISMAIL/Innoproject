from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
app_name='user'
urlpatterns=[
    path('register/',views.register,name="register"),
    path('login/',views.user_login,name="login"),
    path('logout/',views.user_logout,name="logout"),
    path('profile/',views.profile,name="profile"),
    path('add-new-request/',views.newRequest,name="newRequest"),
    path('add-new-donation/',views.newDonation,name="newDonation"),
    path('delete-post/<int:post_id>/',views.delete_request_post,name="delete_post"),
    path('update-post/<int:post_id>/',views.update_post,name="update_post"),
    path('notifications/',views.show_notif,name="notification"),
    path('requests/detail/<str:slug_title>-id=<int:post_id>/',views.post_detail,name="detail"),
    path('notifications/detail/<int:notif_id>/',views.notif_detail,name="notif_detail"),
    path('my-posts/',views.my_posts,name="myallposts"),
    path('my-profile/<str:username>/',views.my_profile,name="my_profile"),
    path('update-profile/<str:username>/',views.update_profile,name="update_profile"),
    path('search-<str:choice>/<str:title>',views.search,name='search'),
    path('nnssssssd/',views.nots,name="nots"),
    # path('test/',views.rad,name='test'),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)