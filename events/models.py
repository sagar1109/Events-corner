from django.db import models
import datetime
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

class event(models.Model):
    program= models.CharField(max_length=100)
    about=models.TextField()
    time=models.DateTimeField(default=timezone.now)
    venue=models.CharField(max_length=50)
    head=models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.program
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    def get_absolute_url(self):
        return reverse('event-detail', kwargs={'pk': self.pk})