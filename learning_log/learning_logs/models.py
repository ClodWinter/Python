from django.db import models

# Create your models here.
class Topic(models.Model):
	"""docstring for Topic"""
	text = models.CharField(max_length=200)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.text



class Entry(models.Model):
	"""docstring for Entry"""
	topic = models.ForeignKey(Topic,on_delete=models.CASCADE)#django 2.1后需要传递on_delete
	text = models.TextField()#没有字数限制的字符串
	date_added = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural = 'entries'

	def __str__(self):
		if len(self.text)>50:
			return self.text[:50] + "..."
		else:
			return self.text
		
		