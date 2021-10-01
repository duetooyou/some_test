from datetime import datetime, timedelta
from django.utils import dateparse
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView
from rest_framework_xml import renderers
from rest_framework.status import HTTP_400_BAD_REQUEST
from .serializers import UserSerializer, HouseSerializer
from .inspectmodel import Users, Houses


class UserView(ModelViewSet):
    serializer_class = UserSerializer
    queryset = Users.objects.all()

    @action(detail=True)
    def get_user_houses(self, request, pk=None):
        if Users.objects.filter(id=pk).exists():
            user_houses = Users.objects.get(pk=pk).houses
            serializer = HouseSerializer(user_houses, many=True)
            return Response(serializer.data)
        else:
            return Response({'Пользователь не зарегистрирован'})
 
    def perform_update(self, serializer):
        vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        if int(self.request.data['salary']) % 123 > 1 and self.request.data['name'].startswith(vowels):
            serializer.save(salary=int(self.request.data['salary'])*2)
        else:
            serializer.save()

    def partial_update(self, request, *args, **kwargs):
        aim_time = 43200000
        try:
            user_time = dateparse.parse_datetime(self.request.data['date']).time()
            user_time_ms = timedelta(hours=user_time.hour, minutes=user_time.minute).total_seconds() * 1000
        except KeyError:
            return Response('Вы можете обновить только дату пользователя')
        instance = self.get_object()
        serializer = UserSerializer(instance, data=self.request.data, partial=True)
        if serializer.is_valid():
            if user_time_ms > aim_time:
                serializer.save(date=datetime(1990, 1, 1))
            else:
                serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.error)

    def get_view_name(self):
        return 'Пользователи'


class HouseView(ModelViewSet):
    serializer_class = HouseSerializer
    queryset = Houses.objects.all()

    def get_view_name(self):
        return f'Недвижимость'

    def perform_create(self, serializer):
        print(self.request.data['user.name'], Users.objects.get(name=self.request.data['user.name']))
        serializer.save(user=Users.objects.get(name=self.request.data['user.name']))

    def create(self, request, *args, **kwargs):
        try:
            return super(ModelViewSet, self).create(request, *args, **kwargs)
        except ObjectDoesNotExist:
            content = {"Пользователь с данным именем не обнаружен"}
            return Response(content, HTTP_400_BAD_REQUEST)


class UserXMLView(RetrieveAPIView):
    renderer_classes = (renderers.XMLRenderer,)
    queryset = Users.objects.all()
    serializer_class = UserSerializer
