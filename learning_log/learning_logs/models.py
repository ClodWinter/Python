from django.db import models

# Create your models here.
class Topic(models.Model):
	"""docstring for Topic"""
	text = models.CharField(max_length=200)
	date_added = models.DateTimeField(auto_now_add=True)

	def _str_(self):
		return self.text


class Entry(models.Model):
	"""docstring for Entry"""
	topic = models.ForeignKey(Topic)
	text = models.TextField()#没有字数限制的字符串
	date_added = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural = 'entries'

def _str_(self):
	return self.text
		
		