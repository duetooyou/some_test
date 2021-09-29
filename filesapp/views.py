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
        if upload_file_format.upper() in file_formats:
            if upload_file_size < 1000000:
                with Image.open(self.request.FILES['file']) as img:
                    img.save(f"{upload_file_name}"+f".{upload_file_format}")
                return Response({'Файл меньше 1MB'})
            else:
                return Response({'Файл больше 1MB, выберите файл меньше 1MB и повторите попытку'})
        else:
            return Response({'Файл должен быть изображением в формате JPEG, GIF, BMP, JPG, PNG. Повторите попытку'})
