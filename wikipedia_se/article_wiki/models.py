import datetime
from django.utils import timezone

from django.db import models


class Article(models.Model):
    titre = models.OneToOneField(
        'titre_wiki.Titre',
        on_delete=models.CASCADE,
        primary_key=True,
    )
    content = models.TextField(blank=True)
    created_At = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titre
