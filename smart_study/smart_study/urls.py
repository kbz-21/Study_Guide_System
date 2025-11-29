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
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Smart Study System API",           # Your API Title
        default_version='v1',                     # v1
        description="""
        A complete backend for students: notes, to-do lists,
        unit converter (yard ↔ foot, pound ↔ kg) and YouTube video search.  
        All endpoints are token-authenticated and user-scoped.
        """,
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # AUTH APIs
    path('api/v1/auth/', include('users.urls')),  

    # DJANGO BUILT-IN LOGIN PAGES
    path('accounts/', include('django.contrib.auth.urls')),

    # FRONTEND HOME ROUTES
    path('', include('users.urls')),

    # NOTES
    path('api/v1/notes/', include('notes.urls')),
    path('notes/', include('notes.urls')),

    # TODO LIST
    path('api/v1/todolist/', include('todolist.urls')),

    # UNIT CONVERTER
    path('api/v1/unitconverter/', include('unitconverter.urls')),

    # YOUTUBE SEARCH
    path('api/v1/youtubesearch/', include('youtubesearch.urls')),

    # SWAGGER
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    # REDOC
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
