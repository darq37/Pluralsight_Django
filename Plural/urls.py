from django.urls import path, re_path
from .views import game_detail, make_move
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns=[
    re_path(r'detail/(?P<id>\d+)/$', game_detail, name="gameplay_detail"),
    re_path(r'make_move/(?P<id>\d+)/$', make_move, name="gameplay_make_move"),

]