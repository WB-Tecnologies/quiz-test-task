from django.conf.urls import url
from django.contrib.auth import views
from . import views
from quizesite import views as views_q

urlpatterns = [
    url(r'^login/$', views.login),
    url(r'^create/',views.create_user,name="create_user"),
    url(r'^signup/$', core_q.signup,name='signup'),
    url(r'^add_quiz/',views.add_quiz,name="add_quiz"),
    url(r'^add_question/',views.add_question,name="add_question"),

]
