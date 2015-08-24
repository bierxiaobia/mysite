from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import login

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'polls.views.login', name='login'),
    url(r'^home$', 'polls.views.home', name='home'),
    url(r'^picture', 'polls.views.picture', name='picture'),
    url(r'^add_picture', 'polls.views.picture_add', name='add_picture'),
    url(r'^save_picture', 'polls.views.save_picture', name='save_picture'),
    url(r'^article', 'polls.views.article', name='article'),
    url(r'^list_article', 'polls.views.article_list', name='article_list'),
    url(r'^add_article', 'polls.views.article_add', name='article_add'),
    url(r'^writedown', 'polls.views.wirtedown', name='wirtedown'),
    # url(r'^signin/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}, name="signin"),
    # url(r'^signout/$', 'django.contrib.auth.views.logout_then_login', name="signout"),

)
