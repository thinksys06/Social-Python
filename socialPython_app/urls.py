"""socialPython URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from socialPython_app import views

urlpatterns = [

        # for showig the (user_list view)
    path('show_user/', views.user_list.as_view()),
    # for showing the (user_detail view)
    path('show_user/<int:pk>', views.user_detail.as_view()),
    
    # for showig the (profile_list view)
    path('show_profile/', views.profile_list.as_view()),
    # for showing the (profile_detail view)
    path('show_profile/<int:pk>', views.profile_detail.as_view())

]
