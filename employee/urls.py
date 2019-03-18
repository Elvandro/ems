from django.conf.urls import url
from . import views


# List of url functions
urlpatterns=[
    url(r'^$',views.welcome, name='welcome'),
    url(r'^index/', views.index, name='index'),
    url(r'^employee/', views.employee, name='employee'),
    url(r'^update_employee/(?P<pk>\d+)/$', views.update_employee, name='update_employee'),
    url(r'^delete_employee/(?P<pk>\d+)/$', views.delete_employee, name='delete_employee'),
]
