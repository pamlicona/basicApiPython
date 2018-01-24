from django.db import models
from albumes.models import Albumes

# Create your models here.
class Songs(models.Model):
	name = models.CharField(max_length=100)
	albumId = models.ForeignKey(Albumes)