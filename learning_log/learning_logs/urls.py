#定义learning_logs的Url模式

from django.urls import path
from . import views

urlpatterns = [
	path('',views.index,name = 'index'),
	path('topics/',views.topics,name = 'topics'),
	path('^topics/(?P<topic_id>\d+)/$',views.topic,name = 'topic')
]