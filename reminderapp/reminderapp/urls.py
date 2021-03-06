"""Reminderapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from reminder_web_app.views import ReminderViewSet
from rest_framework.routers import DefaultRouter
from reminder_web_app import views

# Routers provide an easy way of automatically determine URL conf.
""" Register endpoint in the api's url.From this one url we can get both ListView and DetailView of the objects."""

router = DefaultRouter()
router.register(r'api/v1',views.ReminderViewSet)

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^',include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    
] + static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT)
