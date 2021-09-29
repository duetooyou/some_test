from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserView, HouseView, UserXMLView


router = DefaultRouter()
router.register('users', UserView, basename='user')
router.register('houses', HouseView, basename='house')


urlpatterns = [
    path('', include(router.urls)),
    path('user-xml/<int:pk>', UserXMLView.as_view(), name='user_xml_view'),
]
