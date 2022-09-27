from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('logout', views.logout_view, name='logout_view'),
    path('settings', views.settings, name='settings'),
    path('upload', views.upload, name='upload'),
    path('profile/<str:user>', views.profile, name='profile'),
    path('like-post', views.like_post, name='like-post'),
    path('follow', views.follow, name='follow'),
    path('search', views.search, name='search'),
]
