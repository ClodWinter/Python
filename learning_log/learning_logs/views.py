from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Topic

# Create your views here.
def index(request):
	return render(request,'learning_logs/index.html')

def topics(request):
	topics = Topic.objects.order_by('date_added')
	content = {'topics':topics}
	return render(request,'learning_logs/topics.html',content)

def topic(request,topic_id):
	topic = Topic.objects.get(id=topic_id)
	entries = topic.entry_set.order_by('-date_added')
	contenx = {'topic':topic,'entries':entries}
	return render(request,'learning_logs/topic.html',contenx)