from django.conf.urls import url
from django.contrib.auth import views
from . import views
from quizesite import views as views_q

urlpatterns = [
    url(r'^$', views.login, name='login'),
    url(r'^login/$', views.login),
    url(r'^create/',views.create_user,name="create_user"),
    url(r'^signup/$', core_q.signup,name='signup'),
    url(r'^add_exam/',views.add_exam,name="add_exam"),

]
