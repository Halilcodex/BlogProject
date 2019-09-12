from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    post_text = models.TextField()
    post_create_date = models.DateTimeField(default=timezone.now)
    post_publish_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.post_publish_date = timezone.now()
        self.save()

    def apprv_cmnts_filter(self):
        return self.comments.filter(approved_comments = True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={'pk':self.pk})
    

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    comment_author = models.CharField(max_length=256)
    comment_text = models.TextField()
    comment_date = models.DateTimeField(default=timezone.now)
    approved_comments = models.BooleanField(default=False)

    def approve_comment(self):
        self.approved_comments = True
        self.save()

    def __str__(self):
        return self.comment_author+" "+"| "+self.comment_text
    
    def get_absolute_url(self):
        return reverse("post_list")
    
