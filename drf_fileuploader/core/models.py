from django.db import models

# Create your models here.
class File(models.Model):
    file = models.FileField(blank=True, null=False)
    def __str__(sef):
        return self.file.name


        

