"""SmartFit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.urls import path

from SmartFit import settings
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login', views.logingin, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('profile', views.lk, name='lk'),
    path('personal/info', views.personalinfo, name='personalinfo'),
    path('personal/programs', views.personalprogramms, name='personalprograms'),
    path('personal/workouts', views.personalworkouts, name='personalworkouts'),
    path('personal/progres', views.personalprogress, name='personalprogres'),
    path('personal/subscription', views.subscription, name='subscription'),
    path('trainers/', views.trainers, name='trainers'),
    path('trainers/<int:trainer_id>', views.trainer, name='trainer'),
    path('programs', views.programs, name='programs'),
    path('programs/<int:program_id>', views.program, name='program'),
    path('subscribe/<int:program_id>', views.subscribe, name='subscribe'),
    path('blog/', views.blog, name='blog'),
    path('start/', views.purchase, name='start'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
