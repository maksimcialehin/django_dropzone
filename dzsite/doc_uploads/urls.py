from django.urls import path
from .views import UploadImage, file_upload_view


urlpatterns = [
    path('', UploadImage.as_view(), name='main-view'),
    path('upload/', file_upload_view, name='upload-view'),
]
