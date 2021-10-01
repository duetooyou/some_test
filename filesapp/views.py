import os
import json
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from PIL import Image


class PictureUploadView(APIView):

    parser_classes = [FileUploadParser]

    def put(self, request):
        file_formats = ('BMP', 'PNG', 'JPG', 'GIF', 'JPEG')
        upload_file = self.request.FILES['file']
        upload_file_size = upload_file.size
        upload_file_name = upload_file.name
        upload_file_format = upload_file.content_type.rsplit('/')[1]
        path = 'friendship/magic/photo'
        if upload_file_format.upper() in file_formats:
            if upload_file_size < 1000000:
                with Image.open(self.request.FILES['file']) as img:
                    img.save(f"{path}/{upload_file_name}"+f".{upload_file_format}")
                return Response({'Файл меньше 1MB'})
            else:
                return Response({'Файл больше 1MB, выберите файл меньше 1MB и повторите попытку'})
        else:
            return Response({'Файл должен быть изображением в формате JPEG, GIF, BMP, JPG, PNG. Повторите попытку'})


class JSONFileView(APIView):

    def post(self, request):
        all_langcode = ['af', 'af-ZA', 'ar', '...']
        print(self.request.data['info'])
        aim_path = 'friendship/magic/'
        json_files = [i.rsplit('.')[0] for i in os.listdir(aim_path) if os.path.isfile(os.path.join(aim_path, i))]
        if self.request.data['filename'] in json_files and self.request.data['info']:
            with open(rf"friendship/magic/{self.request.data['filename']}.json", 'r') as opened:
                data = json.load(opened)
            data['quests'] = self.request.data['info']
            with open(rf"friendship/magic/{self.request.data['filename']}.json", 'w') as opened:
                json.dump(data, opened)
            return Response('Файл успешно изменен')
        elif self.request.data['filename'] in all_langcode:
            with open(rf"friendship/magic/{self.request.data['filename']}.json", 'w') as opened:
                data = {'quests': self.request.data['info']}
                json.dump(data, opened, ensure_ascii=False, indent=4)
            return Response('Файл успешно создан')
        else:
            return Response('Проверьте правильность введенной информации')

    def delete(self, request):
        aim_path = 'friendship/magic/'
        json_files = [i.rsplit('.')[0] for i in os.listdir(aim_path) if os.path.isfile(os.path.join(aim_path, i))]
        if self.request.data['filename'] in json_files:
            os.remove(f"{aim_path}/{self.request.data['filename']}.json")
            return Response('Файл успешно удален')
        else:
            return Response('Выбранного файла нет')
