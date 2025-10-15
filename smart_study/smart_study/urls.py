"""
URL configuration for smart_study project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
    path('api/v1/auth/', include('users.urls')),  # API for auth
    path('accounts/', include('django.contrib.auth.urls')),  # Frontend login/logout
    path('', include('users.urls')),  # Add profile frontend if needed
    path('api/v1/notes/', include('notes.urls')),  # API for notes
    path('notes/', include('notes.urls')),  # Frontend for notes
    path('api/v1/todolist/', include('todolist.urls')),  # API for todo list
    path('api/v1/unitconverter/', include('unitconverter.urls')),  # API for unit converter

    

]
