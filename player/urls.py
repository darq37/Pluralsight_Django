from django.urls import path, re_path
from .views import home, new_invitation, accept_invitation
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [

    path('home/', home, name="player_home"),
    path('login/', LoginView.as_view(template_name="player/login_form.html"), name="player_login"),
    path('logout/', LogoutView.as_view(), name="player_logout"),
    path('invitation/', new_invitation, name="player_new_invitation"),
    re_path(r'accept_invitation/(?P<id>\d+)/$', accept_invitation, name="player_accept_invitation"),
]
