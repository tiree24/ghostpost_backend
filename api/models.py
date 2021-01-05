from django.db import models
from django.utils import timezone

# Create your models here.
class BoastRoast(models.Model):
    post_type = models.BooleanField()
    post_content = models.CharField(max_length=280)
    up_vote = models.IntegerField(default=0)
    down_vote = models.IntegerField(default=0)
    total_votes = models.IntegerField(default=0)
    date_created = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.post_content

