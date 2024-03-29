"""VTH URL Configuration

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
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('1.1qna', include('QnA.urls')),
    path('1.2qnac', include('QnA2.urls')),
    path('2.1try', include('TryMultipleTimes.urls')),
    path('2.2tryb', include('TryAgain.urls')),
    path('3diff', include('TryDifferentView.urls')),
    path('f1insp', include('CommentLine.urls')),
    path('f2strfn', include('StringFunction.urls')),
    path('s1', include('Home.urls')),
    path('se2', include('Home2.urls')),
    path('fin', include('Home3.urls')),
    path('', include('Home.urls')),
]
