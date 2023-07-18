"""
URL configuration for YourQ project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name="index"),
    path('about/', about, name="about"),
    path('allquizzes/', allquizzes, name="allquizzes"),
    path('signup/', signup, name="signup"),
    path('signin/', signin, name="signin"),
    path('signout/', signout, name="signout"),
    path('myquizzes/', myquizzes, name="myquizzes"),
    path('profile/', profile, name="profile"),
    path('createquiz/', createquiz, name="createquiz"),
    path('createquiz_status/', createquiz_status, name="createquiz-status"),
    path('playquiz/<int:quiz_id>', playquiz, name="playquiz"),
    path('playquiz_status/<int:quiz_id>', playquiz_status, name="playquiz-status"),
    path('editquiz/<int:quiz_id>', editquiz, name="editquiz"),
    path('editquiz-confirm/<int:quiz_id>', editquiz_confirm, name="editquiz-confirm"),
    path('editquiz_status/', editquiz_status, name="editquiz-status"),
    path('deletequiz/<int:quiz_id>', deletequiz_confirm, name="deletequiz-confirm"),
    path('deletequiz_status/<int:quiz_id>', deletequiz_status, name="deletequiz-status"),
    path('admin/', admin.site.urls),
]
