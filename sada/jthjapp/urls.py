from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('index_news/', views.News_list_view.as_view()),
    path('team_rank/', views.Team_ranking_view.as_view()),
    path('Index_equip_imgs/', views.Index_Equipment_view.as_view()),
    path('inc_introduce/', views.Inc_introduce_view.as_view()),
    path('inc_culture/', views.Culture_view.as_view()),
    path('culture_img/', views.Culture_routimg_view.as_view()),
    path('all_equipment/', views.All_Equipment_view.as_view()),
    path('show_session/', views.Session_test_view.as_view()),
    #用户登陆
    path('user_login/', views.User_login_view.as_view()),
]
