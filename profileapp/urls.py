from typing import ValuesView
from django.urls import path, include
from rest_framework import routers
from . import views

router=routers.DefaultRouter()
router.register('add',views.ProfileView)
router.register('ppp',views.profilelist, basename='ppp')
urlpatterns = [
    path('', views.index, name = 'home'),
    path('profile/', views.profile, name = 'profile'),
    path('login/', views.login_user, name = 'login'),
    path('register/', views.register_user, name = 'register'),
    path('logout/', views.logout_user, name = 'logout'),
    path('get/',include(router.urls)),
    path('hello/',views.Vi.as_view(),name= 'yes'),
    path('h/',views.list,name= 'list'),
    path('hii/',views.createlist,name='create')

]
