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

#admin.autodiscover()

"""Create a reminder and get list of all reminders"""

reminder_list = ReminderViewSet.as_view({
    'get':'list',
    'post':'create'
    })

"""Get reminder, update contents, delete reminder"""

reminder_detail = ReminderViewSet.as_view({
    'get':'retrieve',
    'put':'update',
    'patch':'partial_update',
    'delete':'destroy'
    })

# Routers provide an easy way of automatically determine URL conf.
""" Register reminder url to the router"""

router = DefaultRouter()
router.register(r'api/v1',views.ReminderViewSet)

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^',include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    
]+ static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT)
