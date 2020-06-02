from django.shortcuts import render, get_object_or_404
from .models import Document
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect


def document_menu(request, id, slug):
    documents = Document.objects.filter(available=True)
    document = get_object_or_404(Document, id=id, slug=slug, available=True)
    return render(request, 'navbar/navbar.html', {'documents': documents,
                                                  'document': document,
                                                  })
