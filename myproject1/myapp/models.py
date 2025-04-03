from django.db import models

class Resume(models.Model):
    fullname = models.CharField(max_length=90)  
    email = models.TextField(blank=True, null=True)
    expirience = models.TextField(max_length=255)
    data_field = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.title