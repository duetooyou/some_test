from datetime import datetime, timedelta
from django.utils import dateparse
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView
from rest_framework_xml import renderers
from .serializers import UserSerializer, HouseSerializer
from .models import User, House


class UserView(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    @action(detail=True)
    def get_user_houses(self, request, pk=None):
        if User.objects.filter(id=pk).exists():
            user_houses = User.objects.get(pk=pk).houses
            serializer = HouseSerializer(user_houses, many=True)
            return Response(serializer.data)
        else:
            return Response({'Пользователь не зарегистрирован'})

    def perform_update(self, serializer):
        aim_time = 43200000
        vowels = ('A', 'E', 'I', 'O', 'U')
        user_time = dateparse.parse_datetime(self.request.data['date']).time()
        user_time_ms = timedelta(hours=user_time.hour, minutes=user_time.minute).total_seconds()*1000
        if int(self.request.data['salary']) % 123 > 1 and self.request.data['name'].title().startswith(vowels):
            serializer.save(salary=int(self.request.data['salary'])*2)
        if user_time_ms > aim_time:
            serializer.save(date=datetime(1990, 1, 1))
        else:
            serializer.save()

    def get_view_name(self):
        return 'Пользователи'


class HouseView(ModelViewSet):
    serializer_class = HouseSerializer
    queryset = House.objects.all()

    def get_view_name(self):
        return f'Недвижимость'

    def perform_create(self, serializer):
        serializer.save(owner=User.objects.get(name=self.request.data['owner.name']))


class UserXMLView(RetrieveAPIView):
    renderer_classes = (renderers.XMLRenderer,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
