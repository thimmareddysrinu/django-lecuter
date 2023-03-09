from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.

class Post(models.Model):
                   author=models.ForeignKey('auth.user',on_delete=models.DO_NOTHING)
                   title=models.CharField(max_length=200)
                   text=models.TextField()
                   created_date=models.DateTimeField(default=timezone.now())
                   publish_date=models.DateTimeField(null=True,blank=True)


                   def publish(self):
                                      self.publish_date=timezone.now()
                                      self.save()

                   def approve_comments(self):
                                      return self.comments.fillter(approved_comment=True)

                   def get_absolute_url(self):
                                      return reverse("post_detail", kwargs={"pk": self.pk})
                                      
                   def __str__(self):
                                      return self.title
                                   
class Comment(models.Model):
                   post=models.ForeignKey('blogapp.Post',related_name='comments',on_delete=models.DO_NOTHING)
                   author=models.CharField(max_length=200)
                   text=models.TextField()
                   create_date=models.DateTimeField(default=timezone.now())
                   approved_comment=models.BooleanField(default=False)

                   def approve(self):
                       self.approved_comment = True 
                       self.save()
                   def get_absolute_url(self):
                                      return reverse("post_detail", kwargs={"pk": self.pk})
                   def __str__(self):
                                      return self.text
                                              
                                        


 