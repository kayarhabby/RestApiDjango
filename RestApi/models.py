from django.db import models

# Create your models here.

class Team(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="blog/team/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name