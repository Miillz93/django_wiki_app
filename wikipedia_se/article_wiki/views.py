from django.http import HttpResponse
from django.shortcuts import render
import wikipedia
from time import sleep
import logging
# from django.apps import apps

from .models import Article
from titre_wiki.models import Titre


def article_index(request):
    # titre = apps.get_model('titre_wiki', 'Titre')
    lan = wikipedia.set_lang("fr")
    titre = Titre.objects.all()
    # logger = logging.getLogger(__name__)

    for t in titre:
        try:
            content = wikipedia.page(t.header).content
            # article = Article
            # page =  wikipedia.summary(t.header, sentences=2)
            # t = Article(titre=t.id, content=content)
            # t.save()
            # print(type(type(t.header)))
            # logger.error(t.id)
            # logger.error(t.header)
        except ValueError:
            print(".......")

    return HttpResponse("Article request")
