from django.http import HttpResponse
from django.shortcuts import render, redirect
import logging
import wikipedia
from .models import Titre

# Effectuer 100 enregistrement par rapport à un mot clé saisi via wikipedia API
def titre_index(request):
    logger = logging.getLogger(__name__)
    lan = wikipedia.set_lang("fr")
    if request.method == 'GET':
        titre = Titre.objects.all()
        return render(request, 'titre_wiki/index.html', {'titre': titre, })
    elif request.method == 'POST':
        rechercher = request.POST.get('Rechercher')
        research = wikipedia.search(rechercher, results=100)
        for x in research:
            t = Titre(header=x)
            t.save()
            # logger.error(x)
        return redirect('titre_wiki/index.html')