from django.urls import path
from .views import Uploads, file_upload_view


urlpatterns = [
    path('', Uploads.as_view(), name='main-view'),
    path('upload/', file_upload_view, name='upload-view'),
]
