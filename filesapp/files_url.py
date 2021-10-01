from django.urls import path
from .views import PictureUploadView, JSONFileView


urlpatterns = [
    path('upload/', PictureUploadView.as_view()),
    path('json-files/', JSONFileView.as_view()),
]
