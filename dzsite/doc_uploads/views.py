from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from .models import Uploads


class UploadImage(TemplateView):
    template_name = 'doc_uploads/main.html'


def file_upload_view(request):
    print(request.FILES)
    if request.method == 'POST':
        upload_file = request.FILES.get('file')
        Uploads.objects.create(upload=upload_file)
        return HttpResponse('Successful upload')
    return HttpResponse('upload')
