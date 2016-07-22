from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from reminder_web_app import views

urlpatterns = [
    url(r'^api/v1/$', views.ReminderList.as_view(), name='reminder_list'),
    url(r'^api/v1/(?P<pk>[0-9]+)/$', views.ReminderDetail.as_view(), name='reminder_detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
