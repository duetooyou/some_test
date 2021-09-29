from django.urls import path
from .views import PictureUploadView

urlpatterns = [
    path('upload/', PictureUploadView.as_view())
]
