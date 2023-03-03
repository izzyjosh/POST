from django.db import models
from django.contrib.auth.models  import User


class Posts(models.Model):
	post = models.TextField()
	p_owner = models.ForeignKey(User, on_delete=models.CASCADE)
	
	def __str__(self):
		return self.post
		
class Comment(models.Model):
	comment = models.CharField(max_length=120)
	c_owner = models.ForeignKey(Posts, on_delete=models.CASCADE)
	
	def __str__(self):
		return self.comment