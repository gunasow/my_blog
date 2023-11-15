from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Blog(models.Model) :
    topic = models.CharField(max_length=200)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.topic}-\n{self.text[:50]}...'

class Comment(models.Model) :
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE)
    comment = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    class Meta :
        verbose_name_plural = 'comments'

    def __str__(self):
        return self.comment