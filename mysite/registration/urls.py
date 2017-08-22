from django.conf.urls import url
from django.contrib.auth import views
from . import views


urlpatterns = [
    url(r'^login/$', views.login),
    #url(r'^add_quiz/',views.add_quiz,name="add_quiz"),
    #url(r'^add_question/',views.add_question,name="add_question"),
]
