"""
URL configuration for music_blog project.

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
from django.urls import path, include
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.staticfiles.urls import static
from django.contrib.sitemaps import views
from .sitemaps import SongSitemap
sitemaps={"song": SongSitemap()}
urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path("pages/", include("django.contrib.flatpages.urls")),
        path("sitemap.xml", views.index, {"sitemaps": sitemaps}, name="django.contrib.sitemaps.views.index"),
        path('sitemap-<section>.xml', views.sitemap, {"sitemaps": sitemaps}, name="django.contrib.sitemaps.views.sitemap"),
        ]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)