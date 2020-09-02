import datetime
from django.utils import timezone

from django.db import models


class Titre(models.Model):
    header = models.CharField(max_length=255)
