from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse


class Uploads(TemplateView):
    template_name = 'doc_uploads/main.html'


def file_upload_view(request):
    print(request.FILES)
    return HttpResponse('upload')
